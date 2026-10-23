import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("=" * 60)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("RANDOM FOREST MODEL TRAINING")
print("=" * 60)

# 1. Load the cleaned dataset
df = pd.read_csv("Dataset_cleaned.csv")

# 2. Separate features and target
X = df.drop(columns=["Class"])
y = df["Class"].map({"Good": 0, "Bad": 1})

if y.isnull().any():
    raise ValueError("Unexpected target labels found in the Class column.")

# 3. Split the original data before encoding
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# 4. Prepare categorical and numerical features
categorical_features = ["Fruit"]
numerical_features = [
    "Temp",
    "Humid (%)",
    "Light (Fux)",
    "CO2 (pmm)"
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "fruit_encoder",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        ("numeric_features", "passthrough", numerical_features)
    ]
)

# 5. Create the Random Forest pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42,
                class_weight="balanced"
            )
        )
    ]
)

# 6. Train the model
print("\nTraining the model...")
model.fit(X_train, y_train)

# 7. Predict the test records
y_pred = model.predict(X_test)

# 8. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL EVALUATION")
print("-" * 40)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        y_pred,
        labels=[0, 1],
        target_names=["Good", "Bad"],
        zero_division=0
    )
)

print("\nConfusion Matrix:")
print("Rows = actual classes; columns = predicted classes")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))

# 9. Save the complete pipeline
joblib.dump(model, "food_spoilage_model.pkl")

print("\nModel saved as food_spoilage_model.pkl")
print("MODEL TRAINING COMPLETED!")