import cv2
from PIL import Image

from util import get_limts

yellow = [0,255,255] # yellow in BGR colorspace
#blue = [255,0,0]
red = [0,0,255]
#green = [0,255,0]

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()

  hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
  #colors = [yellow,blue,red,green]
  #for color in colors:
  lower_limit , upper_limit = get_limts(color=yellow)


  mask = cv2.inRange(hsvImage,lower_limit,upper_limit)

  mask_ = Image.fromarray(mask)

  bbox = mask_.getbbox()
    #print(bbox)
  if bbox is not None:
    x1,y1,x2,y2 = bbox

    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),5)


  cv2.imshow('frame',frame)


  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

