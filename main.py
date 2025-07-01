from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load an official model
images = "data/test-images"

# Predict with the model
results = model.predict(source=images, save=True, show=False)

# Access the results
for result in results:
    boxes = result.boxes

    xyxy = boxes.xyxy
    confs = boxes.conf  # confidence scores
    clses = boxes.cls   # class indices
    names = [result.names[int(c)] for c in clses]

    print(f"File: {result.path}")
    for i in range(len(xyxy)):
        print(f"  Object: {names[i]}, Conf: {confs[i]:.2f}, Box: {xyxy[i].tolist()}")
