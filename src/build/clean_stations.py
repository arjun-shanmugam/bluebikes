"""
Clean stations data.
"""
import pandas as pd


# set constants
RAW_STATION_DATA = "/Users/ashanmu1/Documents/GitHub/bluebikes/data/raw/stations/current_bluebikes_stations.csv"

# load station data
station_df = pd.read_csv(RAW_STATION_DATA, skiprows=1)

