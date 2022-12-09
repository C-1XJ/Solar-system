import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")
sun = " sun "
mercury = "mercury"
venus = " venus"
earth = " earth "
mars = " mars "
jupiter = " jupiter"
saturn = " saturn"
uranus = " uranus"
neptune = " neptune"

cv2.putText(
    img,
    sun, 
    (2,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    mercury,
    (100,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    venus,
    (150,250),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    earth,
    (255,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    mars,
    (350,250),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    jupiter,
    (475,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    saturn,
    (675,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    uranus,
    (900,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.putText(
    img,
    neptune,
    (1100,200),
    fontFace=cv2.FONT_HERSHEY_DUPLEX,
    fontScale=1,
    color=(255,255,255)
)

cv2.imshow("solar-system.jpg",img)
cv2.waitKey(0)