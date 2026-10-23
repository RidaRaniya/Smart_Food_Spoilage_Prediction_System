import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD THE CLEANED DATASET
# ==========================================

df = pd.read_csv("food_spoilage_cleaned.csv")

sns.set_theme(style="whitegrid")

print("Creating visualizations...")


# ==========================================
# 2. FOOD TYPE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Food_type",
    order=df["Food_type"].value_counts().index
)

plt.title("Distribution of Food Types")
plt.xlabel("Food Type")
plt.ylabel("Number of Records")
plt.xticks(rotation=30)

plt.tight_layout()
plt.savefig("food_type_distribution.png", dpi=300)
plt.show()


# ==========================================
# 3. AVERAGE EXPIRY DAYS BY FOOD TYPE
# ==========================================

average_expiry = (
    df.groupby("Food_type")["Expiry_days"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=average_expiry.values,
    y=average_expiry.index
)

plt.title("Average Expiry Days by Food Type")
plt.xlabel("Average Expiry Days")
plt.ylabel("Food Type")

plt.tight_layout()
plt.savefig("average_expiry_by_food.png", dpi=300)
plt.show()


# ==========================================
# 4. TEMPERATURE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Temperature",
    bins=30,
    kde=True
)

plt.title("Distribution of Storage Temperatures")
plt.xlabel("Temperature (°C)")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.savefig("temperature_distribution.png", dpi=300)
plt.show()


# ==========================================
# 5. HUMIDITY DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Humidity",
    bins=30,
    kde=True
)

plt.title("Distribution of Humidity")
plt.xlabel("Humidity (%)")
plt.ylabel("Number of Records")

plt.tight_layout()
plt.savefig("humidity_distribution.png", dpi=300)
plt.show()


# ==========================================
# 6. STORAGE CONDITION VS TEMPERATURE
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Storage_condition",
    y="Temperature"
)

plt.title("Temperature by Storage Condition")
plt.xlabel("Storage Condition")
plt.ylabel("Temperature (°C)")

plt.tight_layout()
plt.savefig("storage_temperature.png", dpi=300)
plt.show()


print("\nAll visualizations created successfully!")
print("PNG graphs have been saved in your project folder.")
