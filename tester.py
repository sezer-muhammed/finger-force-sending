from data_manager import DataManager
from reader import FingerForceSensorReader
from plotter import DataVisualiser
import numpy as np
import cv2

#sensor = FingerForceSensorReader("COM3")
#plotter = DataVisualiser()
data_manager = DataManager("empy", "empty.npy")
data_manager.load()
data_manager.set_time()


total_x = 450
total_y = 450

canvas = np.ones((900,900,3), np.uint8) * 255

while True:
  output = data_manager.return_real_time()
  print(output)
  total_x += int(-output[0])
  total_y += int(output[1])
  background = canvas.copy()
  cv2.circle(background, (total_x, total_y), 10, (0,0,255), -1, cv2.LINE_AA)
  cv2.imshow("frame", background)
  cv2.waitKey(1)
