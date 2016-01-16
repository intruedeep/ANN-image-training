import cv2
import numpy as np

def display_image_and_wait(name, img):
  cv2.imshow(name, img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def create_random_image(height, width):
  blank_image = np.zeros((height,width,3), np.uint8)
  #display_image_and_wait("well", blank_image)
  new_image = np.copy(blank_image)
  for i in range(height):
    for j in range(10):
      new_image[i][(i + j)%width] = np.array([255,255,100])

  return new_image

def create_white_image(height, width):
  blank_image = np.zeros((height,width,3), np.uint8)

  return np.array([[[255,255,255] for p in row] for row in blank_image])

if __name__ == "__main__":
  img = create_random_image(1080,1920)
  display_image_and_wait("after!", img)
