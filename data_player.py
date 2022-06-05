from data_manager import DataManager
from plotter import DataVisualiser
import numpy as np

save_path = ""
load_path = "trackpoint_5_haziran.npy"

manager = DataManager(save_path, load_path)
plotter = DataVisualiser()

manager.load()
manager.set_time()

output = np.array([[0, 0, 0]])
filtered_output = np.array([[0, 0, 0]])

def absmaxND(a, axis=None):
    amax = a.max(axis)
    amin = a.min(axis)
    return np.where(-amin > amax, amin, amax)

while True:
  last_output = output
  output = manager.return_all_real_time()
  current_out = output[-1]
  comparison = last_output == output

  if type(comparison) != bool:
    continue

  #output[-1] = np.max(output[-5:])
  if output.shape[0] > 10:
    deneme = np.expand_dims(absmaxND(output[-10:], axis = 0), axis = 0)
    filtered_output = np.concatenate((filtered_output, deneme), axis = 0)

  plotter.render(output)

