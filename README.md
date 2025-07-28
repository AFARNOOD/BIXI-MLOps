# BIXI-MLOps


#  BIXI Trip Duration Prediction using MLOps Pipeline

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Prefect](https://img.shields.io/badge/MLOps-Prefect%203-blue)

<img src="https://github.com/AFARNOOD/BIXI-MLOps/blob/main/imgs/ChatGPT%20Image%20Jul%2028%2C%202025%2C%2001_32_35%20PM.png" width="700" height="468">

---

##  1. Overview

This project demonstrates an end-to-end MLOps pipeline for predicting trip durations in Montreal's BIXI bike-sharing system. Leveraging real-world open datasets from [BIXI Montréal](https://bixi.com/en/open-data), we apply machine learning to forecast how long a bike trip will take based on contextual and spatial features.

The pipeline includes model training, evaluation, deployment via FastAPI, and orchestration using Prefect — all designed to be modular, reproducible, and deployable.

---

##  2. Why this project?

Urban mobility services like BIXI are essential for sustainable and efficient cities. Predicting bike trip durations helps:

- Enhance user experience via better time estimation
- Improve bike redistribution operations
- Support incentive structures and dynamic pricing
- Integrate better into multimodal smart city systems

This project demonstrates how MLOps can be used in real-time transport solutions with public datasets.

---

##  3. Dataset

The data used in this project comes from BIXI Montréal’s official [Open Data Portal](https://bixi.com/en/open-data/). Specifically, the dataset for the **2023 season** was used:

- **Time range:** April–November 2023
- **Trip-level data:** start time, end time, duration, stations, distances
- **Station metadata:** coordinates, arrondissement
- **Format:** CSV

We engineered features such as:

- `trip_distance_km`, `hour`, `day_of_week`, `month`, `is_weekend`
- `start_arrondissement`, `end_arrondissement`
- `station_popularity`, and more

---
## 🚲 Start Station Heatmap

Explore the interactive heatmap of BIXI start stations:

👉 [Click here to open full map](https://afarnood.github.io/BIXI-MLOps/imgs/Top Origin-Destination Pairs.html)
 
[![Heatmap Preview](imgs/heatmap_preview.png)](https://afarnood.github.io/BIXI-MLOps/imgs/Top Origin-Destination Pairs.html)
---

##  4. Problem Statement

The goal is to build a machine learning model that predicts:

> **How long a given BIXI bike trip will take (in minutes), based on trip context**

Using features such as:

- Distance between stations
- Temporal info (hour, day of week, month)
- Popularity and location of start/end stations
- Spatial coordinates and administrative zones

---

##  5. Project Architecture

```plaintextbixi-mlops-project/
BIXI-MLops/
├── app/
│   ├── main.py                   # FastAPI app exposing the prediction API
│   ├── model_loader.py          # Helper function to load the trained model
│
├── imgs/                        # Visual outputs and data visualizations
│   ├── ChatGPT Image Jul 28, 2025, 01_32_35 PM.png
│   ├── Top Origin-Destination Pairs.html
│   ├── start_station_heatmap.html
│
├── model/                       # Trained model artifacts (e.g., .pkl files)
│   └── best_model.pkl           # Output of Prefect pipeline model training
│
├── notebooks/                   # Jupyter notebooks for step-by-step development
│   ├── 01_data_cleaning.ipynb
│   ├── 02_EDA.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_orchestration.ipynb
│   └── mlruns/                  # MLflow experiment tracking output
│
├── pipeline/                    # Prefect flow and task definitions
│   ├── flow.py                  # Prefect flow logic (ETL + ML pipeline)
│   ├── tasks.py                 # Individual Prefect tasks
│   ├── utils.py                 # Helper functions used in pipeline
│   └── __pycache__/             # Python cache (auto-generated)
│
├── .gitignore                   # Git ignored files
├── Dockerfile                   # Docker container specification
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (you’re writing this now)

```

---

##  6. Tech Stack

- Python 3.12
-  JupyterLab
-  Scikit-learn, Pandas, Joblib
-  FastAPI (for API)
-  Prefect 3.0 (for orchestration)
-  Docker (for deployment)

---

##  7. Model Evaluation

Final trained model (Random Forest):

-  **RMSE:** 8.69 minutes
-  **R² Score:** 0.46

This means the model captures nearly half of the variation in trip duration — with potential for improvement using weather/user-type data.

---

##  8. Run the Project Locally

###  8.1. Clone the repository

```bash
git clone https://github.com/your-username/bixi-mlops-project.git
cd bixi-mlops-project
```

###  8.2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

###  8.3. Run the pipeline (via Jupyter or Prefect)

Using Jupyter:

```bash
# Open notebooks/train_model.ipynb
# Run all cells to train and save model
```
Or via Prefect:
```bash
prefect deployment build pipeline/training_flow.py:BIXI-ML-Training-Flow -n dev
prefect deploy
prefect agent start
```

###  8.4. Launch the API
```bash
uvicorn app.main:app --reload
```

Then visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  9. Docker (Optional)
Build the image

```bash
docker build -t bixi-mlops-app .
```
Run the container

```bash
docker run -p 8000:8000 bixi-mlops-app
```

##  10. API Reference

POST `/predict`
Input example:

```bash
{
  "trip_distance_km": 2.5,
  "hour": 17,
  "day_of_week": 5,
  "is_weekend": 0,
  "start_lat": 45.508,
  "start_lon": -73.561,
  "end_lat": 45.511,
  "end_lon": -73.554,
  "start_station_popularity": 10,
  "avg_trip_duration_from_station": 12.3,
  "start_arrondissement": "Ville-Marie",
  "end_arrondissement": "Le Plateau-Mont-Royal",
  "month": 7
}

```
Response:
```bash
{
  "predicted_trip_duration_min": 18.03
}
```

##  11. Limitations & Future Work

- Weather and user-type not yet integrated
- No dynamic model re-training pipeline
- Does not include station-level rebalancing strategies
- Can be extended with a dashboard or React frontend


##  12. Acknowledgements
- BIXI Montréal for releasing such a great open dataset.
- Open-source contributors to FastAPI, Prefect, Scikit-learn, and the Python community.


