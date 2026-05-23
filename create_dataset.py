import requests
import numpy as np
from datetime import datetime, timedelta


def fetch_large_weather_data(lat, lon, days=60):

    end_date = datetime.today()

    start_date = end_date - timedelta(days=days)

    start = start_date.strftime("%Y-%m-%d")
    end = end_date.strftime("%Y-%m-%d")

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}"
        f"&longitude={lon}"
        f"&start_date={start}"
        f"&end_date={end}"
        f"&daily=temperature_2m_mean,"
        f"precipitation_sum,"
        f"wind_speed_10m_max"
        f"&timezone=auto"
    )

    response = requests.get(url)

    return response.json()


def create_sequences(data):

    daily = data['daily']

    temps = daily['temperature_2m_mean']
    rain = daily['precipitation_sum']
    wind = daily['wind_speed_10m_max']

    weather_data = []

    for i in range(len(temps)):

        row = [
            temps[i],
            rain[i],
            wind[i]
        ]

        weather_data.append(row)

    weather_data = np.array(weather_data)

    X = []
    y = []

    # Sliding window
    for i in range(len(weather_data) - 7):

        X.append(weather_data[i:i+7])

        y.append(weather_data[i+7])

    X = np.array(X)
    y = np.array(y)

    return X, y


if __name__ == "__main__":

    lat = 17.3850
    lon = 78.4867

    data = fetch_large_weather_data(lat, lon)

    X, y = create_sequences(data)

    print("X shape:", X.shape)

    print("y shape:", y.shape)