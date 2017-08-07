# -*- coding: utf-8 -*-
# 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import linecache

file = open('source/change_images_size.py', 'r')

fileLines = len(file.readlines())

print('代码行数:%s' % fileLines)

blankLines = 0

for line in range(fileLines):
    if len((linecache.getline('source/change_images_size.py', line).split())) == 0:
        blankLines += 1

print(blankLines)
