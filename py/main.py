import cv2
import numpy as np

def lab00():
    device_id = 0
    cap = cv2.VideoCapture(device_id)

    if not cap.isOpened():
        print(f"Error: Could not open camera {device_id}")
        return
    else:
        print(f"Successfully opened camera {device_id}")

    window_title = "Lab 0: Introduction to Python and OpenCV"
    cv2.namedWindow(window_title, cv2.WINDOW_GUI_NORMAL)

    while True:
        success, frame = cap.read()
        if not success:
            break

        edges = cv2.Canny(frame, 100, 200)

        cv2.imshow(window_title, edges)
        #cv2.imshow(window_title, frame)

        if cv2.waitKey(15) >= 0:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    lab00()
