import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

from create_dataset import (
    fetch_large_weather_data,
    create_sequences
)

# Fetch weather data
lat = 17.3850
lon = 78.4867

data = fetch_large_weather_data(lat, lon)

# Create dataset
X, y = create_sequences(data)

print("X shape:", X.shape)
print("y shape:", y.shape)

# Build model
model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(7,3)
    )
)

model.add(Dense(32, activation='relu'))

model.add(Dense(3))

# Compile
model.compile(
    optimizer='adam',
    loss='mse'
)

# Train
model.fit(
    X,
    y,
    epochs=50,
    batch_size=8
)

# Save model
model.save("weather_model.h5")

print("Model Saved!")