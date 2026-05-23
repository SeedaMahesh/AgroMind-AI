from weather.weather_fetch import fetch_weather
from weather.preprocess import prepare_sequence

lat = 17.3850
lon = 78.4867

# Step 1: Fetch weather
data = fetch_weather(lat, lon)

# Step 2: Convert to LSTM format
X = prepare_sequence(data)

# Print result
print(X)

print(X.shape)