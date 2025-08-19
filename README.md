MRV MVP (Measurement, Reporting, and Verification Minimum Viable Product)

This project implements a Minimum Viable Product (MVP) for a Measurement, Reporting, and Verification (MRV) system focused on agroforestry and rice cultivation. It demonstrates an end-to-end flow from farmer input to carbon calculation and ledger recording.

Features

•
Farmer Data Input: Collects farmer details, area, activity (agroforestry or rice), and optional bounding box information.

•
Mock Satellite NDVI: Includes a mocked satellite NDVI (Normalized Difference Vegetation Index) module for offline demonstration. This can be extended to integrate with real satellite data sources like Google Earth Engine.

•
Carbon Calculation: Computes carbon credits for agroforestry (based on trees planted) and rice (based on water management practices). Placeholder carbon factors are used and can be replaced with IPCC/Verra standards.

•
Hashed Ledger: Records carbon reports in a simple hashed ledger, demonstrating immutability. This can be extended to use decentralized storage solutions like IPFS or public blockchains.

•
Downloadable Reports: Allows users to download calculated carbon reports in CSV format.

Project Structure

Plain Text


mrv-prototype/
├── app.py
├── requirements.txt
├── .gitignore
├── modules/
│   ├── __init__.py
│   ├── carbon_calc.py
│   ├── ledger.py
│   └── satellite.py
├── data/
│   └── farmers_sample.csv
└── reports/
    └── (generated reports and ledger.txt)


•
app.py: The main Streamlit application.

•
requirements.txt: Lists all Python dependencies.

•
.gitignore: Specifies files and directories to be ignored by Git.

•
modules/: Contains modular Python scripts for satellite data, carbon calculation, and ledger management.

•
data/: Stores sample data, such as farmers_sample.csv.

•
reports/: Directory for generated carbon reports and the ledger file.

Setup and Installation

To set up and run this project on your local machine, follow these steps:

1.
Extract the Project Files: Unzip the mrv-prototype.zip file. This will create a folder named mrv-prototype.

2.
Navigate to the Project Directory: Open your terminal or command prompt and change your current directory to the extracted project folder:

3.
Create a Virtual Environment (Recommended): It is highly recommended to create a Python virtual environment to manage project dependencies. This isolates the project's dependencies from your system's global Python packages.

4.
Activate the Virtual Environment: Activate the virtual environment you just created.

•
On macOS and Linux:

•
On Windows (Command Prompt):

•
On Windows (PowerShell):



5.
Install Dependencies: With the virtual environment activated, install all the required Python packages:

Running the Application

Once the setup is complete, you can launch the Streamlit application:

1.
Execute the Streamlit App: From within the mrv-prototype directory (and with your virtual environment activated), run the following command:

2.
Access the Application: Streamlit will start a local server and print a URL in your terminal (e.g., http://localhost:8501). Open this URL in your web browser to access the MRV MVP application.

Customization and Extension

This MVP is designed for easy extension and customization:

•
Real Satellite Data: Replace the mock NDVI logic in modules/satellite.py with actual integrations using libraries like earthengine-api for Google Earth Engine or rasterio for processing Sentinel/Landsat TIFFs.

•
Accurate Carbon Factors: Update the placeholder carbon factors in modules/carbon_calc.py with scientifically validated values from sources like IPCC or Verra.

•
Decentralized Ledger: Integrate modules/ledger.py with decentralized storage solutions (e.g., IPFS) or blockchain testnets for enhanced immutability and transparency.

•
Advanced Verification: Implement additional verification mechanisms, such as photo hashing, GPS EXIF data validation, or machine learning models for fraud detection.

