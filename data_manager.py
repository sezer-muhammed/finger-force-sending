import numpy as np
import time

class DataManager():
  def __init__(self, save_file_name = None, load_file_name = None) -> None:
    self.load_file_name = load_file_name
    self.save_file_name = save_file_name
    self.data = np.empty((0, 3))

  def save(self, data = None):
    np.save(self.save_file_name, data)

  def load(self):
    self.data = np.load(self.load_file_name, allow_pickle = True)
    return self.data

  def set_time(self):
    self.start_time = time.time()

  def return_real_time(self):
    self.last_index = 0
    index_time = time.time() - self.start_time
    try:
      temp_array = self.data[self.data[:, 2] < index_time]
      return temp_array[-1]
    except:
      return np.array([[0, 0, 0]])

  def return_all_real_time(self):
    self.last_index = 0
    index_time = time.time() - self.start_time
    try:
      temp_array = self.data[self.data[:, 2] < index_time]
      if temp_array.size > 0:
        return temp_array
      else:
        pass
    except:
      pass
    return np.array([[0, 0, 0]])