import pandas as pd
from pandas import read_csv


class Coordinate:

    def get_lat_and_long(self, location):
        df = read_csv('weather_data_excel.csv')

        unique_df = df[['Location', 'Lat', 'Long']].drop_duplicates()

        result = unique_df[unique_df['Location'].str.lower() == location.lower()]

        if result.empty:
            return None, None
        else:
            lat = result['Lat'].values[0]
            long = result['Long'].values[0]
            return lat, long