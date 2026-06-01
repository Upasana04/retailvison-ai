from deep_sort_realtime.deepsort_tracker import DeepSort

tracker = DeepSort(max_age=30)

def track_people(frame, detections):

    tracks = tracker.update_tracks(
        [
            (
                [x1, y1, x2-x1, y2-y1],
                det["confidence"],
                "person"
            )
            for det in detections
            for x1,y1,x2,y2 in [det["bbox"]]
        ],
        frame=frame
    )

    results = []

    for track in tracks:

        if not track.is_confirmed():
            continue

        ltrb = track.to_ltrb()

        results.append({
            "id": track.track_id,
            "bbox": ltrb
        })

    return results