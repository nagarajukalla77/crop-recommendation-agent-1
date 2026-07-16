import joblib
import numpy as np


model = joblib.load(
    "models/best_crop_model.pkl"
)

encoder = joblib.load(
    "models/label_encoder.pkl"
)


def predict_crop(features):

    data = np.array(features).reshape(1,-1)

    prediction = model.predict(data)

    crop = encoder.inverse_transform(prediction)

    return crop[0]