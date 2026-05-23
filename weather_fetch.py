import requests
from datetime import datetime, timedelta


def fetch_weather(lat, lon):

    # Last 7 days
    end_date = datetime.today()
    start_date = end_date - timedelta(days=6)

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

    data = response.json()

    return data


if __name__ == "__main__":

    lat = 17.3850
    lon = 78.4867

    data = fetch_weather(lat, lon)

    print(data)