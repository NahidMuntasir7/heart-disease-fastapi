from fastapi import FastAPI
from app.schemas import HeartData
from app.model_loader import predict_heart_disease

app = FastAPI(title="Heart Disease Prediction API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {
        "model": "Random Forest Classifier",
        "features": [
            "age", "sex", "cp", "trestbps", "chol", "fbs",
            "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
        ],
    }

@app.post("/predict")
def predict(data: HeartData):
    result = predict_heart_disease(data)
    return {"heart_disease": result}
