import cv2
import pickle

 

imcap = cv2.VideoCapture(0) 

imcap.set(3, 480) # set width as 640 

imcap.set(4, 360) # set height as 480 

count = 70

for i in range(140): 

    count = count + 1 

    while True: 

        ret, frame = imcap.read()

        cv2.imshow('frame', frame) 

        key = cv2.waitKey(100)

        if key == ord('q') or key == 27: # Esc 

            break

    print(count) 

    file_name = 'image_clo' +str(count) + '.jpg' 

    cv2.imwrite("close/" + file_name, frame) 

    cv2.waitKey(2000) 

imcap.release() 

cv2.destroyWindow('frame') 

cv2.destroyAllWindows() 