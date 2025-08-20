#!/usr/bin/env python3
"""
Demo:
    - Read data from CSV
    - Calculate across the rows
"""

import pathlib
import pandas as pd


data_path = pathlib.Path(__file__).parent / "data" / "people.csv"
assert data_path.exists()
df = pd.read_csv(data_path)

print("\n# Raw Data")
print(data_path.read_text())

print("\n# Initial Dataframe")
print(df)

print("\n# Calculate Body Mass Index (BMI)")
df["bmi"] = df["weight"] / (df["height"]**2)
print(df)


