import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

temperature = np.random.uniform(60, 95, n)
pressure = np.random.uniform(5, 10, n)
speed = np.random.uniform(1000, 1800, n)
vibration = np.random.uniform(1, 6, n)
energy = np.random.uniform(50, 100, n)
raw_material = np.random.uniform(80, 120, n)

waste_score = (
    0.06 * (temperature - 60)
    + 0.015 * (speed - 1000)
    + 0.30 * vibration
    + 0.08 * (energy - 50)
    + 0.10 * (pressure - 5)
)

noise = np.random.normal(0, 2, n)

waste_score = waste_score + noise

waste = (waste_score > 13).astype(int)
quality = 100 - waste_score + np.random.normal(0, 2, n)

data = pd.DataFrame({
    "temperature": temperature,
    "pressure": pressure,
    "speed": speed,
    "vibration": vibration,
    "energy_consumption": energy,
    "raw_material_usage": raw_material,
    "production_quality": quality,
    "waste": waste
})

data.to_csv("manufacturing_data.csv", index=False)

print("Dataset created successfully!")
print(f"Number of records: {len(data)}")
print("\nFirst 5 records:")
print(data.head())