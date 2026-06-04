# RetailVision AI

## Overview
cd

Features:

* Person Detection using YOLOv8
* Multi-frame Tracking using DeepSORT
* Zone Detection
* Visitor Journey Analytics
* Heatmap Analytics
* Conversion Funnel
* Anomaly Detection
* React Dashboard

---

## Tech Stack

Backend:

* Python
* FastAPI
* SQLite

Computer Vision:

* YOLOv8
* DeepSORT
* OpenCV

Frontend:

* React
* Vite
* Recharts

---

## Running Detection Pipeline

### 1. Activate Environment

```bash
cd backend
venv\Scripts\activate
```

### 2. Run Detection Pipeline

```bash
cd pipeline
python run.py
```

The system will:

* Detect visitors
* Track visitors
* Detect zone transitions
* Generate events
* Store events in SQLite

---

## Run API Server

```bash
cd backend
uvicorn app.main:app --reload
```

Swagger:

http://127.0.0.1:8000/docs

---

## Run Dashboard

```bash
cd frontend
npm install
npm run dev
```

Dashboard URL:

http://localhost:5173

---

## APIs

* /metrics
* /events
* /visitor/{id}
* /heatmap
* /funnel
* /anomalies

