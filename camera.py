import cv2
import time

def get_frame():
    cap = cv2.VideoCapture(0)
    time.sleep(1)
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("Camera not working")
        return None, None
    
    cv2.imwrite("current_frame.jpg", frame)
    print("📸 Photo taken")
    return frame, None