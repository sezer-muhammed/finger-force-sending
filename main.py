from matplotlib.pyplot import plot
from reader import FingerForceSensorReader
from plotter import DataVisualiser
import time
import numpy as np


sensor = FingerForceSensorReader("COM3")
plotter = DataVisualiser()


line = []
while True:
  output = sensor.get_all_data()
  plotter.render(output)