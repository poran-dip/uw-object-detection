# Underwater Object Detection using Reinforcement Learning

This is a project that uses YOLOv8, Intel RealSense, and Jetson Nano to detect coordinates and type of object underwater.

## Model Weights

This project uses [YOLOv11n](https://github.com/ultralytics/ultralytics) as the base model.

## Setting Up
1. Clone this repo:
```bash
git clone https://github.com/poran-dip/uw-object-detection
cd uw-object-detection
```

2. Set up virtual environment:
```bash
python -m venv venv

venv\Scripts\activate # Windows
source venv/bin/activate # Mac OS

pip install -r requirements.txt
```

3. Run test detection
```bash
python main.py
```
