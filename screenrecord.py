import cv
import numpy as np
from PIL import ImageGrab
## SCREEN RECORDER AND VIDEO WRITER ##
def screenRecorder():
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter("output.avi", fourcc, 5.0 ,(1980 , 1080))

    while True:
        img = ImageGrab.grab()
        img_np = np.array(img)
        frame = cv.cvtColor(img_np , cv.COLOR_BGR2RGB)
        cv.imshow("Screen recorder", frame)
        out.write(frame)

        if cv.waitKey(1) == 2

    out.release()
    cv.destroyAllWindows()
 
screenRecorder()


