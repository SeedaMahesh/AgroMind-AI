import numpy as np


def prepare_sequence(data):

    # Extract daily data
    daily = data['daily']

    # Get feature arrays
    temps = daily['temperature_2m_mean']
    rain = daily['precipitation_sum']
    wind = daily['wind_speed_10m_max']

    sequence = []

    # Combine features day by day
    for i in range(len(temps)):

        row = [
            temps[i],
            rain[i],
            wind[i]
        ]

        sequence.append(row)

    # Convert to numpy array
    sequence = np.array(sequence)

    # Reshape for LSTM
    sequence = sequence.reshape(1, 7, 3)

    return sequence