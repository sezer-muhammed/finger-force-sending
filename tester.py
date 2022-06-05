from data_manager import DataManager
from reader import FingerForceSensorReader
from plotter import DataVisualiser
import numpy as np
import cv2

save_path = "trackpoint_5_haziran"
load_path = ""

sensor = FingerForceSensorReader("COM3")
manager = DataManager(save_path, load_path)
plotter = DataVisualiser()

total_x = 450
total_y = 450

canvas = np.ones((900,900,3), np.uint8) * 255

for i in range(15000):
  output = sensor.get_all_data()
  plotter.render(output)
  print(i)
manager.save(output)

