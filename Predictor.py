import numpy as np
import pandas as pd
from joblib import load


class Predictor:

    def predict_rain_probability(self, temp, humidity, wind_speed, date, location):

        # Load in model and encoder
        self.rain_probability_model = load('rain_probability_predictor.pkl')
        self.location_encoder = load('location_encoder.pkl')

        # Convert Date
        date = pd.to_datetime(date)

        # Extract the day, and month from date
        day = date.day
        month = date.month
        year = date.year

        location_encoder = self.location_encoder.transform([location])[0]

        use_inputs = pd.DataFrame({
            'Temperature_F' : [temp],
            'Humidity_pct' : [humidity],
            'Wind_Speed_kmh' : [wind_speed],
            'Month' : [month],
            'Day': [day],
            'Year' : [year],
            'Location_encoded' : [location_encoder]
        })

        probability_of_rain = self.rain_probability_model.predict_proba(use_inputs)[:,1][0] * 100

        return probability_of_rain



    


