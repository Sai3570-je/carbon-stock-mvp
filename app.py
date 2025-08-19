# app.py
import streamlit as st
import pandas as pd
import os
import json
from modules import satellite, carbon_calc, ledger

# Ensure folders
os.makedirs("data", exist_ok=True)
os.makedirs("reports", exist_ok=True)

REPORT_CSV = "reports/carbon_report.csv"
LEDGER_FILE = "reports/ledger.txt"

st.set_page_config(page_title="MRV MVP", layout="wide")
st.title("MRV MVP — Agroforestry & Rice (Laptop Demo)")

st.markdown("""
This demo runs fully on your laptop. It uses a mock satellite NDVI if no raster is present.
Fill farmer details, optionally paste a bounding box, and click *Submit*.
""")

with st.form("farmer_form"):
    name = st.text_input("Farmer name", value="Raju")
    farmer_id = st.text_input("Farmer ID (any unique id)", value="F001")
    area_ha = st.number_input("Area (ha)", min_value=0.01, value=0.5, step=0.1, format="%.3f")
    crop = st.selectbox("Activity", ["Agroforestry", "Rice"])
    trees = 0
    water_mgmt = "Continuous flooding"
    if crop == "Agroforestry":
        trees = st.number_input("New trees planted (count)", min_value=0, value=10, step=1)
    if crop == "Rice":
        water_mgmt = st.selectbox("Water management (affects CH4)", ["Continuous flooding", "Alternate Wetting & Drying (AWD)", "Dry seeding / Intermittent"])
    bbox_text = st.text_area("Optional bounding box for farm (minx,miny,maxx,maxy). Leave blank for mock NDVI.", value="")
    photo = st.file_uploader("Optional: Upload a farm photo", type=["png", "jpg", "jpeg"])
    submitted = st.form_submit_button("Submit")

if submitted:
    # parse bbox if provided
    bbox = None
    if bbox_text.strip():
        try:
            vals = [float(x.strip()) for x in bbox_text.strip().split(",")]
            if len(vals) == 4:
                bbox = tuple(vals)
            else:
                st.error("BBox must be 4 numbers: minx,miny,maxx,maxy")
        except Exception as e:
            st.error("Could not parse bbox: " + str(e))

    with st.spinner("Calculating NDVI and carbon..."):
        mean_ndvi = satellite.get_mean_ndvi(bbox=bbox)  # returns float 0..1
        if crop == "Agroforestry":
            result = carbon_calc.compute_agroforestry_credit(area_ha=area_ha, trees=trees, mean_ndvi=mean_ndvi)
        else:
            result = carbon_calc.compute_rice_credit(area_ha=area_ha, water_mgmt=water_mgmt, mean_ndvi=mean_ndvi)

    # compose report
    report = {
        "farmer_id": farmer_id,
        "farmer_name": name,
        "area_ha": area_ha,
        "activity": crop,
        "trees": int(trees),
        "water_management": water_mgmt,
        "mean_ndvi": round(float(mean_ndvi), 4),
        "carbon_tCO2e": round(float(result["tco2e"]), 4),
        "notes": result.get("note", ""),
    }

    # append to CSV
    df_row = pd.DataFrame([report])
    if os.path.exists(REPORT_CSV):
        df_all = pd.read_csv(REPORT_CSV)
        df_out = pd.concat([df_all, df_row], ignore_index=True)
    else:
        df_out = df_row
    df_out.to_csv(REPORT_CSV, index=False)

    # ledger hashing
    h = ledger.append_ledger(report, ledger_file=LEDGER_FILE)

    st.success(f"Calculated {report['carbon_tCO2e']} tCO2e. Report hash: {h[:16]}...")
    st.json(report)

    st.download_button("Download full report CSV", data=open(REPORT_CSV, "rb").read(), file_name="carbon_report.csv", mime="text/csv")

# Show existing reports
if os.path.exists(REPORT_CSV):
    st.subheader("All reports")
    df = pd.read_csv(REPORT_CSV)
    st.dataframe(df)
else:
    st.info("No reports yet. Submit one above.")

st.markdown("---")
st.markdown("**Notes for extension:** To use real satellite data, implement `modules/satellite.py` using Google Earth Engine or reading a Sentinel/Landsat TIFF and compute NDVI per polygon.")

