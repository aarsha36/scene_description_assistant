from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Use small model for real-time

def detect_objects(frame):
    results = model(frame)
    labels = []

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            labels.append(label)

    return list(set(labels))  # Remove duplicates
