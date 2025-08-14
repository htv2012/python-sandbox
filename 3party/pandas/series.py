import pandas as pd


grades = pd.Series([89.3, 78.5, 90.1, 85.0], index=["Anna", "Ben", "Claire", "Dan"])

print("\n# Raw")
print(grades)

print("\n# Some attributes")
print(f"{grades.array=}")
print(f"{grades.dtype=}")
print(f"{grades.empty=}")
print(f"{grades.flags=}")
print(f"{grades.index=}")
print(f"{grades.name=}")
print(f"{grades.shape=}")
print(f"{grades.size=}")
print(f"{grades.values=}")

print("\n# Series can act like a dictionary")
for name, grade in grades.items():
    print(f"{name:<8}: {grade}")
