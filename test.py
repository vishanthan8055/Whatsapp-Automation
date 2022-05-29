import subprocess
import cv2
import matplotlib.pyplot as plt

def image_position(img_src,img_templ):
    plt.rc('font', family='Youyuan', size='9')
    plt.rc('axes', unicode_minus='False')

    for method in range(6):

        result = cv2.matchTemplate(img_src, img_templ, method)

        min_max = cv2.minMaxLoc(result)
        if method == 0 or method == 1:
            match_loc = min_max[2]
        else:
            match_loc = min_max[3]

        right_bottom = (match_loc[0] + img_templ.shape[1], match_loc[1] + img_templ.shape[0])
        # print('result.min_max:', min_max)
        # print('match_loc:', match_loc)
        # print('right_bottom', right_bottom)
        img_disp = img_src.copy()
        cv2.rectangle(img_disp, match_loc, right_bottom, (0, 255, 0), 5, 8, 0)
        cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX, -1)
        cv2.circle(result, match_loc, 10, (255, 0, 0), 2)
    return right_bottom

def click(tap_x, tap_y):
    adb("adb shell input tap {} {}".format(tap_x, tap_y))

def adb(command):
    proc = subprocess.Popen(command.split(' '), stdout=subprocess.PIPE, shell=True)
    (out, _) = proc.communicate()
    return out.decode('utf-8')

# phone='+919150412204'
# message='Hi!!...this is from my script'
#
# # adb(f'adb shell input keyevent 26')
# # adb(f'adb shell input keyevent 82')
# # adb(f'adb shell input text vishanthan')
# # adb(f'adb shell input keyevent 66')
#
# adb(f'adb shell am start -a android.intent.action.VIEW -d "https://api.whatsapp.com/send?phone={phone}"')
# adb('ping 127.0.0.1 -n 3 > nul')
#
# adb(f'adb shell input text "{message}"')
# adb(f'adb shell input keyevent 22 adb shell input keyevent 22  adb shell input keyevent 66')
# # adb(f'adb shell screencap -p /sdcard/screen.png')
# # adb(f'adb pull /sdcard/screen.png screen.png')
img_src = cv2.imread('Student-1.jpg')
img_templ = cv2.imread('Student-1.jpg')
# # x,y= (image_position(img_src,img_templ))
# # x,y=(1041, 2224)
# # click(x,y)
# print(f'Message sent to {phone}')
from bigO import BigO
from random import randint

lib = BigO()
complexity = lib.test(image_position, "random")
complexity = lib.test(image_position, "sorted")
complexity = lib.test(image_position, "reversed")
complexity = lib.test(image_position, "partial")
complexity = lib.test(image_position, "Ksorted")