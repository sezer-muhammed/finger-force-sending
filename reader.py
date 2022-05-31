import serial
import time
import threading
import numpy as np

class FingerForceSensorReader():
  def __init__(self, port_name, baudrate = 115200, timeout = 0.05) -> None: #COM3
    self.port_name = port_name
    self.baudrate = baudrate
    self.timeout = timeout
    self.serial_port = serial.Serial(port = self.port_name, baudrate = self.baudrate, timeout = self.timeout)
    self.start_time = time.time()

    self.sensor_outputs = [[0, 0, 0]]
    self.data_number = -1

    self.threader()
    
  def threader(self):
    self.thread = threading.Thread(target=self.data_reader, daemon=True)
    self.thread.start()

  def data_reader(self):
    while True:
      self.sensor_input = self.serial_port.readline().decode("utf-8")[:-2].split("  ")
      if len(self.sensor_input) > 1:
        self.sensor_input = [int(x) for x in self.sensor_input]
        self.sensor_input.append(time.time() - self.start_time)
        self.sensor_outputs.append(self.sensor_input)
      else :
        self.sensor_outputs.append([0, 0, time.time() - self.start_time])

  def get_all_data(self):

    self.data_number = len(self.sensor_outputs) - 2
    return np.array(self.sensor_outputs)

  def get_most_recent_data(self):
    self.data_number = len(self.sensor_outputs) - 2
    return np.array(self.sensor_outputs[-1])

  def get_next_data(self):
    self.data_number += 1
    return np.array(self.sensor_outputs[self.data_number])
