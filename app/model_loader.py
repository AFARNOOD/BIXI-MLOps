import os
import joblib  # ← ADD THIS LINE
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "best_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
