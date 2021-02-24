# import cv2
#
# cap = cv2.VideoCapture('WIN_20201210_15_32_11_Pro.mp4')
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     cv2.imshow('image', frame)
#     k = cv2.waitKey(0)
#     # q键退出
#     if (k & 0xff == ord('q')):
#         break
#
# cap.release()
# cv2.destroyAllWindows()



import cv2
# import numpy as np

vc = cv2.VideoCapture("WIN_20201208_09_00_48_Pro.mp4")
c = 0
if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False
while rval:
    rval, frame = vc.read()

    # frame=np.rot90(frame)
    # frame=np.rot90(frame)
    # frame=np.rot90(frame)

    cv2.imwrite("WIN_20201208_09_00_48_Pro" + '/' + "%05d" % c + '.jpg', frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
