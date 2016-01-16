import time
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *
from threading import Thread
import sys
import cv2

# The code that the thread executes goes here:
def generate_video_from_images(images, timestep):
  height, width, three = images[0].shape

  fig = plt.figure(1)
  ax = fig.add_subplot(111)
  ax.set_title("ScanPattern")

  im = ax.imshow(np.zeros((height, width, 3)), interpolation='nearest') # Blank starting image
  fig.show()
  im.axes.figure.canvas.draw()

  x = 0
  for image in images:
    #Colors for video.
    # H = np.array(sim.grid)[::]
    # D = np.zeros((NROWS,NCOLS,3))
    # for r in range(len(H)):
    #   for c in range(len(H[r])):
    #     D[r][c] = sim.get_rgb_color(H[r][c])

    #Place data for video.
    ax.set_title( str( x ) )
    im.set_data( image )
    im.axes.figure.canvas.draw()

    x += 1
    time.sleep(timestep)

def show_video_from_images_opencv(images, timestep):
  height, width, three = images[0].shape

  # fig = plt.figure(1)
  # ax = fig.add_subplot(111)
  # ax.set_title("ScanPattern")

  # im = ax.imshow(np.zeros((height, width, 3)), interpolation='nearest') # Blank starting image
  # fig.show()
  # im.axes.figure.canvas.draw()

  x = 0
  for image in images:
    cv2.imshow('frame',image)
    if cv2.waitKey(timestep) & 0xFF == ord('q'):
        break

  time.sleep(10)
    #Colors for video.
    # H = np.array(sim.grid)[::]
    # D = np.zeros((NROWS,NCOLS,3))
    # for r in range(len(H)):
    #   for c in range(len(H[r])):
    #     D[r][c] = sim.get_rgb_color(H[r][c])

    #Place data for video.
    # ax.set_title( str( x ) )
    # im.set_data( image )
    # im.axes.figure.canvas.draw()

    # x += 1
    # time.sleep(timestep)