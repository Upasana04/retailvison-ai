## Architecture

CCTV Video
→ YOLOv8 Detection
→ DeepSORT Tracking
→ Zone Detection
→ Event Generation
→ SQLite Database
→ FastAPI APIs
→ React Dashboard

---

## Detection Layer

YOLOv8 is used to detect people from CCTV footage.

## Tracking Layer

DeepSORT assigns persistent visitor IDs across frames.

## Zone Detection

Store zones are defined using coordinates and visitor center points are mapped to zones.

## Event Generation

The system generates:

* ENTRY
* ZONE_ENTER
* ZONE_EXIT

events whenever visitors move through the store.

## Database

Events are stored in SQLite.

## Analytics

The backend generates:

* Visitor Metrics
* Heatmap
* Funnel Analytics
* Anomaly Detection
* Visitor Journey

## AI-Assisted Decisions

AI assistance was used to:

* Compare object detection models
* Evaluate tracking approaches
* Discuss event schema design
* Review API structure
* Assist with dashboard planning

All final implementation, debugging, testing, and integration decisions were manually performed and validated.
