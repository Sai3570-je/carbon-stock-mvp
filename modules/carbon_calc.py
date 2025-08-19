# modules/carbon_calc.py
"""
Simple carbon calculator for demo:
- Agroforestry: uses a placeholder average biomass per tree.
- Rice: uses placeholder methane reduction factors (tCO2e per ha) by water management type.

Replace placeholders with real IPCC/Verra factors for production use.
"""

def compute_agroforestry_credit(area_ha, trees, mean_ndvi):
    """
    Very simple heuristic:
      - avg_biomass_per_tree_kg : placeholder (e.g., 100 kg)
      - biomass_to_carbon = 0.5
      - carbon_to_co2 = 3.67
    """
    avg_biomass_per_tree_kg = 120  # placeholder; calibrate for species/age
    total_biomass_kg = trees * avg_biomass_per_tree_kg
    total_carbon_kg = total_biomass_kg * 0.5
    tco2e = total_carbon_kg / 1000.0 * 3.67
    note = f"Used avg_biomass_per_tree={avg_biomass_per_tree_kg}kg; mean_ndvi={mean_ndvi}"
    return {"tco2e": tco2e, "note": note}

def compute_rice_credit(area_ha, water_mgmt, mean_ndvi):
    """
    Placeholder approach for rice methane reduction:
    - Continuous flooding baseline CH4 emission factor (placeholder)
    - AWD reduces CH4 by some factor -> convert to tCO2e avoided
    Use IPCC Tier-1 or Verra VM for proper numbers.
    """
    # placeholder emission factors (tCO2e/ha per season) - NOT REAL
    baseline_ch4_tco2e_per_ha = 1.0  # placeholder baseline per season
    if water_mgmt == "Continuous flooding":
        eff = 1.0
    elif "AWD" in water_mgmt:
        eff = 0.5  # 50% reduction placeholder
    else:
        eff = 0.8

    avoided_per_ha = baseline_ch4_tco2e_per_ha * (1.0 - eff)
    total_avoided = avoided_per_ha * area_ha
    note = f"placeholder rice model; eff={eff}; mean_ndvi={mean_ndvi}"
    return {"tco2e": total_avoided, "note": note}


