import pandas as pd
import numpy as np
import os

# Define column names; Note iput file is tabular

# Column 1: time (UTC)
# Column 2: pressure (hPa)
# Column 3: temperature (C)
# Column 4: relative humidity (%)
# Column 4b: relative humidity
# Column 6: wind speed (m/s)
# Column 7: wind direction (degrees)
# Column 13: dewpoint (C)
col_names = ['time', 'pressure', 'temperature', 'relative_humidity', 'rh',
             'speed', 'direction', 'geopot', 'dewpoint']

# Define the input file