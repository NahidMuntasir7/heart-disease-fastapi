import joblib
import numpy as np

# Load trained model
model = joblib.load("model/heart_model.joblib")

def predict_heart_disease(data):
    values = np.array([list(data.dict().values())]).reshape(1, -1)
    pred = model.predict(values)[0]
    return bool(pred)