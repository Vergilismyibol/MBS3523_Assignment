import cv2
import numpy as np


# Rest of your code...
cam = cv2.VideoCapture(0)

desired_width = 480
desired_height = 360

# 設定攝像頭的寬度和高度
cam.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

# 確認設定後的寬度和高度
width = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("新的攝像頭寬度：", width)
print("新的攝像頭高度：", height)

cv2.namedWindow("Multiple Flipped Frames")

while True:

    ret, frame = cam.read()
    width = cam.get(3)  # columnq
    height = cam.get(4)  # Row

    splitFrame = np.zeros((2 * frame.shape[0], 2 * frame.shape[1], 3), np.uint8)

    frame_flip_horizontal = cv2.flip(frame, 1)
    # splitFrame[:int(height / 2), :int(width / 2)] = frameResize

    frame_flip_vertical = cv2.flip(frame, 0)
    # frameFlip0 = cv2.cvtColor(frameFlip0, cv2.COLOR_BGR2HSV)
    # splitFrame[int(height / 2):, :int(width / 2)] = frameFlip0

    frame_flip_both = cv2.flip(frame, -1)
    # frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_BGR2GRAY)
    # frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_GRAY2BGR)
    # splitFrame[:int(height / 2), int(width / 2):] = frameFlip1

    # frameFlip2 = cv2.flip(frameResize, -1)
    # frameFlip2 = cv2.GaussianBlur(frameFlip2, (25, 25), 0)
    # splitFrame[int(height / 2):, int(width / 2):] = frameFlip2


    splitFrame[0:frame.shape[0], 0:frame.shape[1]] = frame
    splitFrame[0:frame.shape[0], frame.shape[1]:2 * frame.shape[1]] = frame_flip_horizontal
    splitFrame[frame.shape[0]:2 * frame.shape[0], 0:frame.shape[1]] = frame_flip_vertical
    splitFrame[frame.shape[0]:2 * frame.shape[0], frame.shape[1]:2 * frame.shape[1]] = frame_flip_both

    cv2.imshow("Multiple Flipped Frames", splitFrame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


# import cv2
# import numpy as np
# import time
#
# cam = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cam.read()
#     width = cam.get(3)  # columnq
#     height = cam.get(4)  # Row
#
#     splitFrame = np.zeros(frame.shape, np.uint8)
#     frameResize = cv2.resize(frame, (int(width / 2), int(height / 2)))
#     splitFrame[:int(height / 2), :int(width / 2)] = frameResize
#
#     frameFlip0 = cv2.flip(frameResize, 0)
#     frameFlip0 = cv2.cvtColor(frameFlip0, cv2.COLOR_BGR2HSV)
#     splitFrame[int(height / 2):, :int(width / 2)] = frameFlip0
#
#     frameFlip1 = cv2.flip(frameResize, 1)
#     frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_BGR2GRAY)
#     frameFlip1 = cv2.cvtColor(frameFlip1, cv2.COLOR_GRAY2BGR)
#     splitFrame[:int(height / 2), int(width / 2):] = frameFlip1
#
#     frameFlip2 = cv2.flip(frameResize, -1)
#     frameFlip2 = cv2.GaussianBlur(frameFlip2, (25, 25), 0)
#     splitFrame[int(height / 2):, int(width / 2):] = frameFlip2
#
#     cv2.putText(splitFrame, "Original", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#     cv2.putText(splitFrame, "Vertical Flip + HSV output", (5, 30 + int(height / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#                 (255, 255, 255), 2)
#     cv2.putText(splitFrame, "Horizontal Flip + Gray", (5 + int(width / 2), 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#                 (0, 255, 0), 2)
#     cv2.putText(splitFrame, "Double Flip + Gaussian Blur", (5 + int(width / 2), 30 + int(height / 2)),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
#     cv2.imshow("Multiple outputs", splitFrame)
#
#     cur_time = time.time()
#     key = cv2.waitKey(1)
#
#     if key == ord('q'):
#         break
#     elif key == ord('s'):
#         cv2.imwrite('screencap_{}.jpg'.format(cur_time), splitFrame)
#
# cam.release()
# cv2.destroyAllWindows()