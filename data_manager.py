import numpy as np
import time

class DataManager():
  def __init__(self, save_file_name = None, load_file_name = None) -> None:
    self.load_file_name = load_file_name
    self.save_file_name = save_file_name
    self.data = np.empty((0, 3))

  def save(self, data = None):
    if data != None:
      self.data = data
    np.save(self.save_file_name, self.data)

  def load(self):
    self.data = np.load(self.load_file_name, allow_pickle = True)
    return self.data