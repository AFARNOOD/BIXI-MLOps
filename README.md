# BIXI-MLOps


# 🚴‍♀️ BIXI Trip Duration Prediction using MLOps Pipeline

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![Prefect](https://img.shields.io/badge/MLOps-Prefect%203-blue)

---

## 📌 Overview

This project demonstrates an end-to-end MLOps pipeline for predicting trip durations in Montreal's BIXI bike-sharing system. Leveraging real-world open datasets from [BIXI Montréal](https://bixi.com/en/open-data), we apply machine learning to forecast how long a bike trip will take based on contextual and spatial features.

The pipeline includes model training, evaluation, deployment via FastAPI, and orchestration using Prefect — all designed to be modular, reproducible, and deployable.

---

## 🎯 Why this project?

Urban mobility services like BIXI are essential for sustainable and efficient cities. Predicting bike trip durations helps:

- Enhance user experience via better time estimation
- Improve bike redistribution operations
- Support incentive structures and dynamic pricing
- Integrate better into multimodal smart city systems

This project demonstrates how MLOps can be used in real-time transport solutions with public datasets.

---

## 📊 Dataset

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

## ❓ Problem Statement

The goal is to build a machine learning model that predicts:

> **How long a given BIXI bike trip will take (in minutes), based on trip context**

Using features such as:

- Distance between stations
- Temporal info (hour, day of week, month)
- Popularity and location of start/end stations
- Spatial coordinates and administrative zones

---

## 🏗️ Project Architecture

