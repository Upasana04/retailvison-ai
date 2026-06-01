import cv2

from detect import detect_people
from tracker import track_people

video_path = "../videos/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    detections = detect_people(frame)

    tracks = track_people(frame, detections)

    for track in tracks:

        x1, y1, x2, y2 = map(int, track["bbox"])

        track_id = track["id"]

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"ID:{track_id}",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    cv2.imshow("RetailVision AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()