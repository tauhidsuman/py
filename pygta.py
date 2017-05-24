import numpy as np
#from PIL import ImageGrab
import pyscreenshot as ImageGrab
import cv2
import time
#import directkeys as dk

def draw_lines(img, lines):
    try: 
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]),(coords[2],coords[3]), [255,0,0], 3)
    except:
        pass

def roi(img, vertices): #region of interest
    mask = np.zeros_like(img) #fill array similar to img with zeroes
    cv2.fillPoly(mask, vertices, 255) #fill area within vertices with 255
    masked = cv2.bitwise_and(img, mask) #bitwise AND operation; only img area within mask will have data
    return masked

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY) #convert to gray
    processed_img = cv2.Canny(processed_img, threshold1=10, threshold2=75) #edge detection
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0)
    vertices = np.array([[0,0],[0,600],[800,600],[800,0]]) #screen space to include
    processed_img = roi(processed_img, [vertices])

    #                       edges
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180, np.array([]), 100, 5)
    draw_lines(processed_img, lines)
    
    return processed_img

last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0,40,1152,864))) #grab the screenshot
    new_screen = process_img(screen)

    cv2.imshow('window2', new_screen) #pump the grabbed screen into a new window
    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
       cv2.destroyAllWindows() #close windows and exit when 'q' is pressed
       break
