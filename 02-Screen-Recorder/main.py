import cv2
import numpy as np
import pyautogui

SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("recording.avi", fourcc, 20.0, (SCREEN_SIZE))

print("Recording... Press 'q' to stop.")

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    if cv2.waitKey(1) == ord("q"): break

out.release()
cv2.destroyAllWindows()
print("Saved as recording.avi")