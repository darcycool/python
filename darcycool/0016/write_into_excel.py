# -*- coding: utf-8 -*-
# 第 0016 题： 纯文本文件 numbers.txt, 里面的内容（包括方括号），请将上述内容写到 numbers.xls 文件中
import collections
import json

import xlwt

with open('numbers.txt', 'r') as f:
    data = json.load(f)
    print(data)

wb = xlwt.Workbook()
ws = wb.add_sheet('number')

for index, item in enumerate(data):
    for j, value in enumerate(item):
        print(index, j, value)
        ws.write(index, j, value)

wb.save('numbers.xls')
