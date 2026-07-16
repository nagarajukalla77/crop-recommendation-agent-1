import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset

df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Dataset Loaded")
print(df.head())


# Separate features and target

X = df.drop("label", axis=1)
y = df["label"]


# Encode target

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)


# Split data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)


# Train model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


model.fit(X_train, y_train)


# Check accuracy

prediction = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    prediction
)

print("Accuracy:", accuracy)


# Create models folder

os.makedirs("models", exist_ok=True)


# Save model

joblib.dump(
    model,
    "models/best_crop_model.pkl"
)


# Save encoder

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)


print("Model Saved Successfully")