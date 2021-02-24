# import numpy as np
# import cv2

# path = 'E:/A_infrared/infrared_py/WIN_20201210_15_32_11_Pro/'
# path_hongwai = path + 'hongwai/'
# path_kejian = path + 'kejian/'

# window = np.zeros(6, dtype=float)

# for i in range(1, 14836):
#     j = i%6
#     frame = cv2.imread(path + "%05d"%i + '.jpg')
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
#     gray_value = np.mean(gray)
#     window[j] = gray_value
    
#     if j==5:
#         index_max = np.argmax(window)
#         index_min = np.argmin(window)
#         frame_hongwai = cv2.imread(path + "%05d"%(i-5+index_max) + '.jpg')
#         frame_kejian = cv2.imread(path + "%05d"%(i-5+index_min) + '.jpg')
#         cv2.imwrite(path_hongwai + '/' + "%05d"%(i-5+index_max) + '.jpg', frame_hongwai)
#         cv2.imwrite(path_kejian + '/' + "%05d"%(i-5+index_min) + '.jpg', frame_kejian)
        


import numpy as np
import cv2

path = 'E:/A_infrared/infrared_py/WIN_20201208_09_00_48_Pro/'
path_hongwai = path + 'hongwai/'
path_kejian = path + 'kejian/'

window = np.zeros(6, dtype=float)

for i in range(1, 9508):
    # j = (i-1)%6
    j = i%6
    frame = cv2.imread(path + "%05d"%i + '.jpg')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    gray_value = np.mean(gray)
    window[j] = gray_value
    
    if j==5:
        index_max = np.argmax(window)
        index_min = np.argmin(window)
        frame_hongwai = cv2.imread(path + "%05d"%(i-5+index_max) + '.jpg')
        frame_kejian = cv2.imread(path + "%05d"%(i-5+index_min) + '.jpg')
        # cv2.imwrite(path_hongwai + '/' + "%05d"%((i-1)/6) + '.jpg', frame_hongwai)
        # cv2.imwrite(path_kejian + '/' + "%05d"%((i-1)/6) + '.jpg', frame_kejian)
        cv2.imwrite(path_hongwai + '/' + "%05d"%(i/6) + '.jpg', frame_hongwai)
        cv2.imwrite(path_kejian + '/' + "%05d"%(i/6) + '.jpg', frame_kejian)
        
        