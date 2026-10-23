import pandas as pd

# ==========================================
# 1. LOAD THE CLEANED DATASET
# ==========================================

df = pd.read_csv("food_spoilage_cleaned.csv")

print("=" * 60)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("DATA ANALYSIS")
print("=" * 60)


# ==========================================
# 2. FOOD TYPE DISTRIBUTION
# ==========================================

print("\n1. NUMBER OF RECORDS FOR EACH FOOD TYPE")

print(df["Food_type"].value_counts())


# ==========================================
# 3. STORAGE CONDITION ANALYSIS
# ==========================================

print("\n2. NUMBER OF RECORDS FOR EACH STORAGE CONDITION")

print(df["Storage_condition"].value_counts())


# ==========================================
# 4. PACKAGING ANALYSIS
# ==========================================

print("\n3. NUMBER OF RECORDS FOR EACH PACKAGING TYPE")

print(df["Packaging"].value_counts())


# ==========================================
# 5. TEMPERATURE ANALYSIS
# ==========================================

print("\n4. TEMPERATURE STATISTICS")

print(df["Temperature"].describe())


# ==========================================
# 6. HUMIDITY ANALYSIS
# ==========================================

print("\n5. HUMIDITY STATISTICS")

print(df["Humidity"].describe())


# ==========================================
# 7. EXPIRY DAYS ANALYSIS
# ==========================================

print("\n6. EXPIRY DAYS STATISTICS")

print(df["Expiry_days"].describe())


# ==========================================
# 8. AVERAGE EXPIRY DAYS BY FOOD TYPE
# ==========================================

print("\n7. AVERAGE EXPIRY DAYS BY FOOD TYPE")

average_expiry = df.groupby("Food_type")["Expiry_days"].mean()

print(average_expiry.round(2).sort_values(ascending=False))


# ==========================================
# 9. AVERAGE TEMPERATURE BY STORAGE CONDITION
# ==========================================

print("\n8. AVERAGE TEMPERATURE BY STORAGE CONDITION")

average_temperature = df.groupby("Storage_condition")["Temperature"].mean()

print(average_temperature.round(2))


# ==========================================
# 10. AVERAGE HUMIDITY BY STORAGE CONDITION
# ==========================================

print("\n9. AVERAGE HUMIDITY BY STORAGE CONDITION")

average_humidity = df.groupby("Storage_condition")["Humidity"].mean()

print(average_humidity.round(2))


print("\nDATA ANALYSIS COMPLETED!")
