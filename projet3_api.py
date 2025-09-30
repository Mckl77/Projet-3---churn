from fastapi import FastAPI
from pathlib import Path
import joblib
from pydantic import BaseModel

# Définir l'application FastAPI
app = FastAPI()

# Définir le chemin du modèle sauvegardé
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "artifacts_models" / "best_random_forest_pipeline.joblib"

# Charger le modèle
model = joblib.load(MODEL_PATH)

# Définir une classe pour les données d'entrée
class CustomerData(BaseModel):
    
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float

@app.get("/")
def read_root():
    return {"message": "✅ API Churn fonctionne !"}

@app.post("/predict")
def predict(data: CustomerData):
    # Transformer l'input en dataframe compatible avec le pipeline
    import pandas as pd
    input_df = pd.DataFrame([data.dict()])

    # Faire une prédiction avec le modèle
    prediction = model.predict(input_df)
    proba = model.predict_proba(input_df)[:, 1]

    return {
        "prediction": int(prediction[0]),
        "probability": float(proba[0])
    }
