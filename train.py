from image import display_image_and_wait, create_random_image, create_white_image
import numpy as np
from video import generate_video_from_images, show_video_from_images_opencv
import cv2
from log import setup_log_to_console
from constants import log
import logging

DEBUG_LOGLEVEL = logging.DEBUG
WARNING_LOGLEVEL = logging.WARNING
LOGFORMAT_STRING = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

def train_truenorth_with_array(arr):
  """
  Sends training data to truenorth neurons.
  """
  print("shape is: %s"%(str(arr.shape)))
  print("arr[0]: %s"%(str(arr[0])))
  display_image_and_wait("hey!", arr)


def train_truenorth_with_image(pixels):
  """
  Trains truenorth with given image.
  INPUT:
    Pixels: np.ndarray([height, width]) of pixel values in (R,G,B)
  """
  img_height, img_width, three = pixels.shape
  for i in range(9):
    for j in range(16):
      arr = np.zeros((img_height, img_width, 3))
      print("pixels.shape: %s"%(str(pixels.shape)))
      print("arr.shape: %s"%(str(arr.shape)))
      for y in range(0,img_height,9):
        for x in range(0,img_width,16):
          arr[y + i][x + j] = pixels[i + y][x + j]

      train_truenorth_with_array(np.array(arr))


def get_truenorth_training_images(pixels, ratio,n):
  """
  Trains truenorth with given image.
  INPUT:
    Pixels: np.ndarray([height, width]) of pixel values in (R,G,B)
  """
  retarr = []
  img_height, img_width, three = pixels.shape
  arr = np.zeros((img_height, img_width, 3))
  # for i in range(9):
  #   for j in range(16):
  for i in range(ratio[0]*ratio[0]):
    for j in range(ratio[1]*ratio[1]):
      arr = np.copy(arr)
      # arr = np.zeros((img_height, img_width, 3))
      # print("pixels.shape: %s"%(str(pixels.shape)))
      # print("arr.shape: %s"%(str(arr.shape)))
      for y in range(0,img_height,ratio[0]*ratio[0]):
        for x in range(0,img_width,ratio[1]*ratio[1]):
          arr[y + i][x + j] = pixels[i + y][x + j]
          
      log.debug("pixels[:3]: %s"%(str(pixels[:3])))
      log.debug("arr[:3]: %s"%(str(arr[:3])))

      retarr.append(arr)

  return np.array(retarr, np.uint8)

if __name__ == "__main__":
  setup_log_to_console(DEBUG_LOGLEVEL,LOGFORMAT_STRING)
  img = cv2.imread("../Resources/Images/teamphoto-better-res.jpg", cv2.IMREAD_COLOR)
  cv2.imshow("before", img)
  log.debug("img.shape: %s"%(str(img.shape)))
  #img = create_white_image(1080,1920)
  #display_image_and_wait("whiteness", img)
  log.debug("getting multiplexed images...")
  images = get_truenorth_training_images(img, [2,3], 3)
  log.debug("done getting images..")
  log.debug("showing video...")
  show_video_from_images_opencv(images, 100)
  log.debug("exiting!")


