# Technical Choices

## Model Selection

### Chosen Model

YOLOv8n

### Alternatives Considered

* YOLOv5
* Faster R-CNN

### Reason

YOLOv8n provides fast inference and sufficient accuracy for real-time retail analytics.

---

## Tracking Selection

### Chosen

DeepSORT

### Alternatives Considered

* SORT
* ByteTrack

### Reason

DeepSORT combines motion prediction with appearance embeddings, improving visitor identity consistency.

---

## Schema Design

Events Table:

* id
* visitor_id
* event_type
* zone
* timestamp

Reason:

An event-based schema is simple, compact, and supports multiple analytics such as visitor journeys, heatmaps, and funnels.

---

## API Design Decision

Chosen Endpoint:

GET /funnel

Reason:

Conversion analysis is an important retail metric. The funnel endpoint calculates how many visitors reached the cash counter compared to total entries.

Alternative Considered:

Computing conversion rates in the frontend.

Reason Rejected:

Business logic should remain in the backend to ensure consistency and maintainability.
