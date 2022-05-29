from reader import FingerForceSensorReader
from plotter import DataVisualiser
import numpy as np
import cv2

sensor = FingerForceSensorReader("COM3")
#plotter = DataVisualiser()

total_x = 450
total_y = 450

canvas = np.ones((900,900,3), np.uint8) * 255

while True:
  output = sensor.get_most_recent_data()
  total_x += int(-output[0])
  total_y += int(output[1])
  background = canvas.copy()
  print(total_x, total_y)
  cv2.circle(background, (total_x, total_y), 10, (0,0,255), -1, cv2.LINE_AA)
  cv2.imshow("frame", background)
  cv2.waitKey(1)