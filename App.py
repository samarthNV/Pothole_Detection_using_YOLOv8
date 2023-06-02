from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import torch
import torchvision.transforms as transforms
from PIL import Image

model = YOLO("C:/Users/VN/Desktop/Projects/Pothole_Detection/best.pt")
result = model.predict(source="0", show=True, conf=0.8)
print(result)