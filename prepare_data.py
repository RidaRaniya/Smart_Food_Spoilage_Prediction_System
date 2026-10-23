import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

print("=" * 55)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("MACHINE LEARNING DATA PREPARATION")
print("=" * 55)

# 1. Load the cleaned dataset
df = pd.read_csv("Dataset_cleaned.csv")

# 2. Separate input features and target
X = df.drop(columns=["Class"])
y = df["Class"].map({"Good": 0, "Bad": 1})

# 3. Identify categorical and numerical columns
categorical_columns = ["Fruit"]
numerical_columns = [
    "Temp",
    "Humid (%)",
    "Light (Fux)",
    "CO2 (pmm)"
]

# 4. Encode the fruit names
encoder = OneHotEncoder(
    handle_unknown="ignore",
    sparse_output=False
)

encoded_fruits = encoder.fit_transform(X[categorical_columns])

encoded_fruits_df = pd.DataFrame(
    encoded_fruits,
    columns=encoder.get_feature_names_out(categorical_columns)
)

# 5. Combine encoded categories with numerical features
X_prepared = pd.concat(
    [
        X[numerical_columns].reset_index(drop=True),
        encoded_fruits_df.reset_index(drop=True)
    ],
    axis=1
)

# 6. Check the prepared data
print("\nOriginal dataset shape:", df.shape)
print("Prepared feature shape:", X_prepared.shape)

print("\nPrepared feature columns:")
print(X_prepared.columns.tolist())

print("\nTarget label counts:")
print(y.value_counts().rename(index={0: "Good", 1: "Bad"}))

print("\nFirst 5 prepared records:")
print(X_prepared.head())

print("\nMissing values in features:", X_prepared.isnull().sum().sum())
print("Missing target values:", y.isnull().sum())

# 7. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_prepared,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

print("\nDATA PREPARATION COMPLETED!")