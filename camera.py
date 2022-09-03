import cv2 
import os
n=input("Enter Your Name: ")
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)
while True:
    try:
        check, frame = webcam.read()
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
        	path='images'
        	cv2.imwrite(filename=n+'.jpg', img=frame)
        	name=n+'.jpg'
        	webcam.release()
        	img_new = cv2.imread(n+'.jpg', 1)
        	cv2.imwrite(os.path.join(path, name), img_new)
        	img_new = cv2.imshow("Captured Image", img_new)
        	cv2.waitKey(1650)
        	cv2.destroyAllWindows()
        	break
        elif key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        
    except(KeyboardInterrupt):
        print("Turning off camera.")
        webcam.release()
        print("Camera off.")
        print("Program ended.")
        cv2.destroyAllWindows()
        break
