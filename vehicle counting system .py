import cv2
import numpy as np
import os

min_contour_width = 40
min_contour_height = 40
offset = 10
line_height = 550
matches = []
cars = 0

def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

cap = cv2.VideoCapture('traffic.mp4')

cap.set(3, 1920)
cap.set(4, 1080)

if not cap.isOpened():
    print("Error opening video file")
    exit()

ret, frame1 = cap.read()
ret, frame2 = cap.read()

car_number = 1
vehicle_numbers = []
labeled_images_dir = "image-labeling"
os.makedirs(labeled_images_dir, exist_ok=True)

while ret:
    # ... (rest of the code)

    # Inside the loop
    # Display the frame using OpenCV
    cv2.imshow('Frame', frame1)
    cv2.waitKey(10)  # Pause for a short time to display the updated frame

    frame1 = frame2
    ret, frame2 = cap.read()

# Release the capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
