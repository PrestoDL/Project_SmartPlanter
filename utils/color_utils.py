import cv2
import numpy as np

def get_avg_color(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (100, 100))
    avg_color = img.mean(axis=0).mean(axis=0)  # BGR
    return avg_color[::-1]  # RGB
