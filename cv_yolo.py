# -*- coding: utf-8 -*-
"""CV_YOLO.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cNSkWqob6L_GUKAKnk50AMwzM-W-SWMf
"""

!pip install torch torchvision torchaudio
!pip install opencv-python
!pip install matplotlib
!pip install yolov5  # from PyPI or clone from GitHub

import torch
import cv2
import matplotlib.pyplot as plt
from google.colab import files

# Load the pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load image
image_path = '/content/Vehicles_waiting_at_a_traffic_signal_at_São_Paulo.jpg'  # Replace with your image path
img = cv2.imread(image_path)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Run detection
results = model(img_rgb)

# Filter for vehicle classes
vehicle_classes = ['car', 'truck', 'bus', 'motorbike']
detections = results.pandas().xyxy[0]
vehicles = detections[detections['name'].isin(vehicle_classes)]

# Draw boxes on original image
for _, row in vehicles.iterrows():
    x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
    label = row['name']
    confidence = row['confidence']
    text = f"{label} {confidence:.2f}"  # Add confidence score
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(img, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Show the result
plt.figure(figsize=(10, 6))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Detected Vehicles')
plt.show()

# Save the image with detections
output_path = '/content/vehicle_detection_result.jpg'
cv2.imwrite(output_path, img)

# Download the image to your computer
files.download(output_path)

