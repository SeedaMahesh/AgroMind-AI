import numpy as np
from tensorflow.keras.models import load_model

from weather_fetch import fetch_weather
from preprocess import prepare_sequence

model = load_model("weather_model.h5", compile=False)

# Location
lat = 17.3850
lon = 78.4867

# Fetch latest weather
data = fetch_weather(lat, lon)

# Convert into LSTM format
X = prepare_sequence(data)

print("Input Shape:", X.shape)

# Predict tomorrow weather
prediction = model.predict(X)

print("\nPredicted Tomorrow Weather:\n")

print("Temperature:", prediction[0][0])

print("Rainfall:", prediction[0][1])

print("Wind Speed:", prediction[0][2])