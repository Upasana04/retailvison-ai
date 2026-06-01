from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_people(frame):

    results = model(frame, verbose=False)

    detections = []

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if cls == 0:  # person

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                conf = float(box.conf[0])

                detections.append(
                    {
                        "bbox": [x1, y1, x2, y2],
                        "confidence": conf
                    }
                )

    return detections