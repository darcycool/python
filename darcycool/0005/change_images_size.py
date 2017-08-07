# -*- coding: utf-8 -*-
# 第 0005 题： 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
import os

from PIL import Image

rootDir = 'imgs/'


def judge_size(img):
    imgSize = img.size
    return max(imgSize) > 1136


def return_size(img):
    max, min = img.size
    if max > min:
        return max, min
    else:
        return min, max


def change_size(img, max, min):
    value = max / 1136
    min = int(min / value)
    newImg = img.resize((1136, min), Image.ANTIALIAS)
    return newImg


for parent, dirnames, filenames in os.walk(rootDir):
    for filename in filenames:
        fName = filename
        print(filename)
        filename = parent + os.sep + filename
        fPostfix = os.path.splitext(filename)[1]
        try:
            img = Image.open(filename)
        except:
            print(filename)
            continue
        # img.load()
        print(filename)
        print(fPostfix)
        if (fPostfix == '.jpg' or fPostfix == '.png' or fPostfix == '.JPG' or fPostfix != '.PNG'):
            print(judge_size(img))
            if (judge_size(img) == True):
                max, min = return_size(img)
                newimg = change_size(img, max, min)
                newimg.save(rootDir + os.sep + fName)
