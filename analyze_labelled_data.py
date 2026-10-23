import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("Dataset_cleaned.csv")

print("=" * 55)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("LABELLED DATASET ANALYSIS")
print("=" * 55)

# 1. Dataset information
print("\n1. DATASET SIZE")
print("Total records:", len(df))
print("Total columns:", len(df.columns))

# 2. Fruit types
print("\n2. RECORDS BY FRUIT TYPE")
print(df["Fruit"].value_counts())

# 3. Class distribution
print("\n3. CLASS DISTRIBUTION")
print(df["Class"].value_counts())

print("\nClass percentages:")
print((df["Class"].value_counts(normalize=True) * 100).round(2))

# 4. Average temperature by class
print("\n4. AVERAGE TEMPERATURE BY CLASS")
print(df.groupby("Class")["Temp"].mean().round(2))

# 5. Average humidity by class
print("\n5. AVERAGE HUMIDITY BY CLASS")
print(df.groupby("Class")["Humid (%)"].mean().round(2))

# 6. Average light by class
print("\n6. AVERAGE LIGHT BY CLASS")
print(df.groupby("Class")["Light (Fux)"].mean().round(2))

# 7. Average CO2 by class
print("\n7. AVERAGE CO2 BY CLASS")
print(df.groupby("Class")["CO2 (pmm)"].mean().round(2))

# 8. Numeric summary
print("\n8. NUMERIC DATA SUMMARY")
print(df[["Temp", "Humid (%)", "Light (Fux)", "CO2 (pmm)"]].describe())

# 9. Save class distribution chart
df["Class"].value_counts().plot(
    kind="bar",
    title="Distribution of Good and Bad Classes",
    xlabel="Class",
    ylabel="Number of Records"
)

plt.tight_layout()
plt.savefig("class_distribution.png", dpi=300)
plt.show()

print("\nAnalysis completed successfully!")
print("Chart saved as class_distribution.png")