from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from prefect import task
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

@task
def load_data():
    X_train = pd.read_csv("data/X_train.csv")
    X_test = pd.read_csv("data/X_test.csv")
    y_train = pd.read_csv("data/y_train.csv").squeeze()
    y_test = pd.read_csv("data/y_test.csv").squeeze()
    return X_train, X_test, y_train, y_test

@task
def train_model(X_train, y_train):
    # Identify categorical columns
    categorical_cols = X_train.select_dtypes(include=['object', 'category']).columns.tolist()

    # Create a preprocessing transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ],
        remainder='passthrough'  # Keep numeric columns as-is
    )

    # Create pipeline: preprocessing + model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42))
    ])

    # Fit the model pipeline
    model.fit(X_train, y_train)
    return model

@task
def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    print(f"✅ RMSE: {rmse:.2f}, R²: {r2:.2f}")
    return rmse, r2

@task
def save_model(model):
    joblib.dump(model, "model/best_model.pkl")
    print("✅ Model saved to model/best_model.pkl")
