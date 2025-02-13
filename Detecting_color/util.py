import numpy as np
import cv2


def get_limts(color):
  c = np.uint8([[color]])
  hsvc = cv2.cvtColor(c,cv2.COLOR_BGR2HSV) # converting to hsv

  hue = hsvc[0][0][0]

  # Handle red hue wrap-around as Red is at both ends of the HSV hue scale (0 and 180)
  if hue >=165:
    lower_limit = np.array([hue-10,100,100],dtype=np.uint8)
    upper_limit = np.array([180,255,255],dtype=np.uint8)

  elif hue <= 15:
    lower_limit = np.array([0,100,100],dtype=np.uint8)
    upper_limit = np.array([hue+10,255,255],dtype=np.uint8)

  else:
    # Dispalys hue range for other than red
    lower_limit = np.array([hue-10,100,100],dtype=np.uint8)
    upper_limit = np.array([hue+10,255,255],dtype=np.uint8)

  return lower_limit,upper_limit
