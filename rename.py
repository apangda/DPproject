import os

path = 'E:/A_infrared/infrared_py/WIN_20201208_16_25_34_Pro/kejian'


def rename(path):
    file_list = os.listdir(path)
    # total_num=len(file_list)
    i = 1
    for item in file_list:
        if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(path), item)
            dst = os.path.join(os.path.abspath(path), format(str(i), '0>5s') + '.jpg')
            # dst = os.path.join(os.path.abspath(path), '%05d%i.jpg')
            try:
                os.rename(src, dst)
                print(i)
                i = i + 1
                
            except:
                continue
            
if __name__ == '__main__':
    rename(path)
    