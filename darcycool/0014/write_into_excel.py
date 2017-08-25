# -*- coding: utf-8 -*-
# 第 0014 题： 纯文本文件 student.txt为学生信息,请将上述内容写到 student.xls 文件中

import json
from collections import OrderedDict

import xlwt

file = open('student.txt', 'r')

students = json.loads(file.read(), object_pairs_hook=OrderedDict)

wb = xlwt.Workbook()
ws = wb.add_sheet('学生信息')

for index, items in enumerate(students.items()):
    ws.write(index, 0, items[0])
    for j, v in enumerate(items[1]):
        ws.write(index, j + 1, v)

wb.save('学生信息.xls')
