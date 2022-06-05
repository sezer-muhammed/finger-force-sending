import matplotlib.pyplot as plt
import numpy as np

class DataVisualiser():
  def __init__(self, seconds = 10) -> None: #COM3
    self.seconds = seconds
    self.fig, self.ax = plt.subplots()
    self.fig.set_figwidth(20)
    self.fig.set_figheight(12)
    self.ax.set_ylim([-100, 100])
    x = np.linspace(-self.seconds, 0, 100)
    (self.ln,) = self.ax.plot(x, x, animated=True)
    plt.show(block=False)
    plt.pause(0.1)
    self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
    self.ax.draw_artist(self.ln)
    self.fig.canvas.blit(self.fig.bbox)

  def data_regularize(self, data):
    if data.shape[0] < 1000:
      return data
    else:
      return data[-1000:]

  def render(self, data):
    data = self.data_regularize(data)
    self.fig.canvas.restore_region(self.bg)
    self.ln.set_xdata(data[:, 2] - data[-1, 2])
    self.ln.set_ydata(data[:, 0])
    self.ax.draw_artist(self.ln)
    self.ln.set_ydata(data[:, 1])
    self.ax.draw_artist(self.ln)
    self.fig.canvas.blit(self.fig.bbox)
    self.fig.canvas.flush_events()