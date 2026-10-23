import pandas as pd

# 1. Load the dataset
df = pd.read_csv("food_spoilage_dataset.csv")

print("=" * 60)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("DATA QUALITY CHECK")
print("=" * 60)

# 2. Check missing values
print("\n1. MISSING VALUES")
print(df.isnull().sum())

print("\nTotal missing cells:", df.isnull().sum().sum())

# 3. Check duplicate rows
print("\n2. DUPLICATE ROWS")
print("Total duplicates:", df.duplicated().sum())

# 4. Check unexpected categorical values
print("\n3. FOOD TYPES")
print(df["Food_type"].value_counts(dropna=False))

print("\n4. STORAGE CONDITIONS")
print(df["Storage_condition"].value_counts(dropna=False))

print("\n5. PACKAGING TYPES")
print(df["Packaging"].value_counts(dropna=False))

# 5. Check numeric ranges
print("\n6. TEMPERATURE RANGE")
print("Minimum:", df["Temperature"].min())
print("Maximum:", df["Temperature"].max())

print("\n7. HUMIDITY RANGE")
print("Minimum:", df["Humidity"].min())
print("Maximum:", df["Humidity"].max())

print("\n8. EXPIRY DAYS RANGE")
print("Minimum:", df["Expiry_days"].min())
print("Maximum:", df["Expiry_days"].max())

# 6. Check whether humidity is outside 0-100%
invalid_humidity = df[
    (df["Humidity"] < 0) |
    (df["Humidity"] > 100)
]

print("\n9. INVALID HUMIDITY VALUES")
print("Number of rows:", len(invalid_humidity))

# 7. Check invalid expiry days
invalid_expiry = df[df["Expiry_days"] <= 0]

print("\n10. INVALID EXPIRY DAYS")
print("Number of rows:", len(invalid_expiry))

# 8. Check invalid purchase dates
dates = pd.to_datetime(
    df["Date_of_purchase"],
    errors="coerce"
)

print("\n11. INVALID PURCHASE DATES")
print("Number of rows:", dates.isna().sum())

print("\nDATA QUALITY CHECK COMPLETED!")
