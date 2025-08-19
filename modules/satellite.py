# modules/satellite.py
"""
Simple satellite module for MVP.
- If a GeoTIFF named data/sample_satellite.tif exists and has at least 4 bands (B2,B3,B4,B8),
  you can extend this file to compute real NDVI per polygon with rasterio.
- For now, this function returns a mock NDVI (0.3 - 0.8) so the app runs offline.
"""

import os
import numpy as np
import rasterio

def get_mean_ndvi(bbox=None):
    """
    Returns mean NDVI for the given bbox.
    - bbox: (minx, miny, maxx, maxy) in the same CRS as your raster (not used in mock).
    If you want to plug real data, replace the mock path logic with rasterio + window read.
    """
    sample_raster = "data/sample_satellite.tif"
    # If a real raster exists, attempt to compute NDVI (basic)
    if os.path.exists(sample_raster):
        try:
            with rasterio.open(sample_raster) as src:
                arr = src.read()
                # This minimal example assumes array bands: (b, rows, cols)
                # and that red = band 3 and nir = band 4 (adjust per your tif)
                # NOTE: real rasters vary; adjust indices accordingly.
                if arr.shape[0] >= 4:
                    red = arr[2].astype("float32")
                    nir = arr[3].astype("float32")
                    denom = (nir + red)
                    denom[denom == 0] = 1e-6
                    ndvi = (nir - red) / denom
                    # If bbox provided, we\'d compute mean over window. For now, use whole array mean.
                    mean_ndvi = float(np.nanmean(ndvi))
                    return float(np.clip(mean_ndvi, -1, 1))
        except Exception as e:
            print("Error reading sample raster:", e)

    # Fallback mock NDVI (so the demo runs offline)
    np.random.seed()  # non-deterministic seed
    mock_ndvi = float(np.round(np.random.uniform(0.25, 0.75), 3))
    return mock_ndvi


