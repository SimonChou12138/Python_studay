# -*- coding:utf-8 -*-
import numpy as np
import cv2
import time
import subprocess


def video2imgs(video_name, size):
    img_list = []

    cap = cv2.VideoCapture(video_name)
    while(True):
        ret, frame = cap.read()
        if ret==True:
            gary = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = cv2.resize(gary, size, interpolation=cv2.INTER_AREA)
            img_list.append(img)
        else:
            break
    cap.release()
    return img_list

pixels = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"


def img2chars(img):
    res = []
    percents = img / 255
    indexs = (percents*(len(pixels)-1)).astype(np.int)
    height, width = img.shape

    for row in range(height):
        line = ""
        for col in range(width):
            index = indexs[row][col]
            line += pixels[index]+""
        res.append(line)
    return res


def imgs2chars(imgs):
    video_chars = []
    for img in imgs:
        video_chars.append(img2chars(img))

    return video_chars


def play_video(video_chars):
    width, height = len(video_chars[0][0]), len(video_chars[0])

    for pic_i in range(len(video_chars)):
        for line_i in range(height):
            print(video_chars[pic_i][line_i])
        time.sleep(1 / 24)

        subprocess.call("cls")


if __name__ == "__main__":
    imgs = video2imgs("cxk.mp4", (64, 48))
    video_chars = imgs2chars(imgs)
    input("转换完成！按enter键")
    # process1 = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
    play_video(video_chars)


