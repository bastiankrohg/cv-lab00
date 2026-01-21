import cv2
import numpy as np

focus_point = None
focus_radius = 80

accumulated = None
alpha = 0.7  # higher = less trail, lower = more ghosting


def on_mouse(event, x, y, flags, param):
    global focus_point
    if event == cv2.EVENT_LBUTTONDOWN:
        focus_point = (x, y)


def lab00():
    global accumulated

    device_id = 0
    cap = cv2.VideoCapture(device_id)

    if not cap.isOpened():
        print(f"Error: Could not open camera {device_id}")
        return
    else:
        print(f"Successfully opened camera {device_id}")

    window_title = "Lab 0: Introduction to Python and OpenCV"
    cv2.namedWindow(window_title, cv2.WINDOW_GUI_NORMAL)
    cv2.setMouseCallback(window_title, on_mouse)

    while True:
        success, frame = cap.read()
        if not success:
            break

        blurred_frame = cv2.GaussianBlur(frame, (21, 21), 0)

        if focus_point is not None:
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.circle(mask, focus_point, focus_radius, 255, -1)
            mask_3ch = cv2.merge([mask, mask, mask])
            focused = np.where(mask_3ch == 255, frame, blurred_frame)
        else:
            focused = blurred_frame

        cv2.imshow(window_title, focused)

        if cv2.waitKey(15) >= 0:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    lab00()
