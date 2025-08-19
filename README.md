# MRV MVP (Measurement, Reporting, and Verification Minimum Viable Product)

This project implements a **Minimum Viable Product (MVP)** for a Measurement, Reporting, and Verification (MRV) system focused on **agroforestry and rice cultivation**. It demonstrates an end-to-end flow from farmer input to carbon calculation and ledger recording.

---

## Features

- **Farmer Data Input**: Collects farmer details, area, activity (agroforestry or rice), and optional bounding box information.  
- **Mock Satellite NDVI**: Includes a mocked satellite NDVI (Normalized Difference Vegetation Index) module for offline demonstration. Can be extended to integrate with real satellite data sources like Google Earth Engine.  
- **Carbon Calculation**: Computes carbon credits for agroforestry (based on trees planted) and rice (based on water management practices). Placeholder carbon factors are used and can be replaced with IPCC/Verra standards.  
- **Hashed Ledger**: Records carbon reports in a simple hashed ledger, demonstrating immutability. Can be extended to use decentralized storage solutions like IPFS or public blockchains.  
- **Downloadable Reports**: Users can download calculated carbon reports in CSV format.  

---

## Project Structure

mrv-prototype/
├── app.py
├── requirements.txt
├── .gitignore
├── modules/
│ ├── init.py
│ ├── carbon_calc.py
│ ├── ledger.py
│ └── satellite.py
├── data/
│ └── farmers_sample.csv
└── reports/
└── (generated reports and ledger.txt)

- `app.py`: Main Streamlit application.  
- `requirements.txt`: Lists all Python dependencies.  
- `.gitignore`: Specifies files and directories to be ignored by Git.  
- `modules/`: Contains modular Python scripts for satellite data, carbon calculation, and ledger management.  
- `data/`: Stores sample data like `farmers_sample.csv`.  
- `reports/`: Directory for generated carbon reports and ledger file.  

---

## Setup and Installation

1. **Extract Project Files**: Unzip `mrv-prototype.zip` to create a folder named `mrv-prototype`.  
2. **Navigate to Project Directory**: Open your terminal and change to the project folder:
   ```bash
   cd mrv-prototype
Create a Virtual Environment (Recommended):

python -m venv venv


Activate Virtual Environment:

macOS / Linux:

source venv/bin/activate


Windows (Command Prompt):

venv\Scripts\activate.bat


Windows (PowerShell):

.\venv\Scripts\Activate.ps1


Install Dependencies:

pip install -r requirements.txt

Running the Application

Run the Streamlit App:

streamlit run app.py


Access the Application: Open the URL printed in your terminal (e.g., http://localhost:8501) in a web browser to access the MRV MVP.

Customization and Extension

Real Satellite Data: Replace the mock NDVI logic in modules/satellite.py with actual integrations using libraries like earthengine-api (Google Earth Engine) or rasterio (for Sentinel/Landsat TIFFs).

Accurate Carbon Factors: Update placeholder carbon factors in modules/carbon_calc.py with scientifically validated values from sources like IPCC or Verra.

Decentralized Ledger: Integrate modules/ledger.py with decentralized storage solutions (e.g., IPFS) or blockchain testnets for enhanced immutability and transparency.

Advanced Verification: Implement additional verification mechanisms such as photo hashing, GPS EXIF validation, or machine learning models for fraud detection.

License

This project is intended for hackathon and educational purposes. Use responsibly.
