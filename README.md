# Heart Disease Prediction API

A **Machine Learning + FastAPI + Docker** project that predicts whether a person is likely to have heart disease based on key health parameters.

This API is built with **FastAPI**, trained using a **Random Forest Classifier**, and containerized with **Docker** for easy deployment.  

It is deployed live on **Render**.

---

## 📘 About This App

This app provides an easy-to-use API for predicting the presence of heart disease.  
It takes medical input features such as **age**, **cholesterol**, **blood pressure**, etc., and returns whether heart disease is likely (`true` or `false`).

The model was trained using the [Heart Disease Dataset on Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset).

---

## 🌍 Live Demo

### 🔗 **Render Deployment:**
👉 [https://heart-disease-fastapi7.onrender.com/](https://heart-disease-fastapi7.onrender.com/)

Visit the `/docs` page to test the APIs using Swagger UI:

👉 [https://heart-disease-fastapi7.onrender.com/docs](https://heart-disease-fastapi7.onrender.com/docs)

---

## ⚙️ API Endpoints

| Method | Endpoint | Description |
|:-------|:----------|:-------------|
| `GET`  | `/health` | Health check (returns status OK) |
| `GET`  | `/info`   | Model details and feature list |
| `POST` | `/predict` | Predicts heart disease based on user input |

### 🧠 Example `/predict` Request:
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 120,
  "chol": 240,
  "fbs": 0,
  "restecg": 1,
  "thalach": 160,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 2
}
```

### ✅ Example Response:
```json
{
  "heart_disease": false
}
```

---

## 🧩 Tech Stack

- **Python**
- **FastAPI** - for the API backend
- **scikit-learn** - for training the model
- **joblib** - for saving/loading the trained model
- **Docker** - for containerization
- **Render** - for live cloud deployment

---

## 🧠 How It Works

1. A machine learning model (Random Forest) is trained on heart disease data.
2. The trained model is saved as `model/heart_model.joblib`.
3. FastAPI loads this model and exposes an endpoint (`/predict`) to make predictions.
4. The app is containerized using Docker and deployed to Render.

---

## 🧰 Project Structure

```
heart-disease-fastapi/
│
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── schemas.py           # Input data model (Pydantic)
│   └── model_loader.py      # Model loading and prediction logic
│
├── model/
│   └── heart_model.joblib   # Trained ML model
│
├── data/
│   └── heart.csv            # Dataset 
│
├── train_model.py           # Script to train and save the model
├── requirements.txt         # Dependencies
├── Dockerfile               # Docker image setup
├── docker-compose.yml       # Docker Compose setup
├── .dockerignore            # Ignored files during Docker build
└── README.md                # Documentation
```

---

## 💻 How to Clone and Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/NahidMuntasir7/heart-disease-fastapi.git
cd heart-disease-fastapi
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

**Activate it:**
- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ (Optional) Retrain the Model

If you want to retrain the model locally:
```bash
python train_model.py
```

### 5️⃣ Run the FastAPI App
```bash
uvicorn app.main:app --reload
```

**Visit:**
👉 http://127.0.0.1:8000/docs

---

## 🐳 Run with Docker

### 1️⃣ Build the Image
```bash
docker-compose build
```

### 2️⃣ Run the Container
```bash
docker-compose up
```

The app will be available at:
👉 http://localhost:8000/docs

### 3️⃣ Stop the Container
```bash
docker-compose down
```

---

## 📊 Model Features

The model uses the following features for prediction:

- **age**: Age of the patient
- **sex**: Gender (1 = male, 0 = female)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure
- **chol**: Serum cholesterol in mg/dl
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = yes, 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of the peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **thal**: Thalassemia (1 = normal, 2 = fixed defect, 3 = reversible defect)

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---







