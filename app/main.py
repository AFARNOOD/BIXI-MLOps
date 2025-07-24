from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.model_loader import load_model

app = FastAPI()
model = load_model()

class TripFeatures(BaseModel):
    trip_distance_km: float
    hour: int
    day_of_week: int
    is_weekend: int
    start_lat: float
    start_lon: float
    end_lat: float
    end_lon: float
    start_station_popularity: int
    avg_trip_duration_from_station: float
    start_arrondissement: str      # <-- NEW
    end_arrondissement: str        # <-- NEW
    month: int                     # <-- NEW

@app.get("/")
def root():
    return {"message": "🚴 BIXI Trip Duration Prediction API"}

@app.post("/predict")
def predict(features: TripFeatures):
    input_df = pd.DataFrame([features.dict()])
    prediction = model.predict(input_df)[0]
    return {"predicted_trip_duration_min": round(prediction, 2)}
