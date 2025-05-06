# YOLOv5 Vehicle Detection 🚗🚌🚚

This Jupyter Notebook demonstrates how to use the YOLOv5 object detection model to detect vehicles (cars, trucks, buses, and motorbikes) in an image. It utilizes a pretrained YOLOv5 model from Ultralytics via `torch.hub`.

## 🔍 Features

- Loads YOLOv5s model (small, fast version) from Ultralytics.
- Detects and labels vehicles from uploaded images.
- Visualizes results using OpenCV and Matplotlib.
- Allows download of annotated images directly in Google Colab.

## 🛠️ Installation

Run these in Google Colab to install dependencies:

```bash
!pip install torch torchvision torchaudio
!pip install opencv-python matplotlib
!pip install yolov5
