import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
import cv2

from detect import detect_people
from tracker import track_people

from events.zone_detector import get_zone

video_path = "../videos/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

printed_shape = False

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Print video resolution once
    if not printed_shape:
        print("Frame Shape:", frame.shape)
        printed_shape = True

    detections = detect_people(frame)

    tracks = track_people(frame, detections)

    for track in tracks:

        x1, y1, x2, y2 = map(int, track["bbox"])

        track_id = track["id"]

        # Center point of person
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        # Detect zone
        zone = get_zone(center_x, center_y)

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

        # Show detected zone
        cv2.putText(
            frame,
            zone,
            (x1, y2 + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

        # Show center point
        cv2.circle(
            frame,
            (center_x, center_y),
            5,
            (0, 0, 255),
            -1
        )

    cv2.imshow("RetailVision AI", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()