import cv2


def lab00():
    device_id = 0
    cap = cv2.VideoCapture(device_id)

    if not cap.isOpened():
        print("Error: Could not open camera {device_id}")
        return
    else:
        print(f"Successfully opened camera {device_id}")

    window_title = "Lab 0: Introduction to Python and OpenCV"
    cv2.namedWindow(window_title, cv2.WINDOW_GUI_NORMAL)

    while True: 
        success, frame = cap.read()

        if not success:
            print("The image capture did not succeed. Is the camera OK?")
            break

        cv2.imshow(window_title, frame)
        delay_ms = 15
        key = cv2.waitKey(delay_ms)

        if key >= 0:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    lab00()
