# -*- coding: utf-8 -*-
# 第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）,请将上述内容写到 city.xls 文件中
import collections
import json

import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('city')

file = open('city.txt', 'r')
city = json.load(file)
print(city)

city = collections.OrderedDict(sorted(city.items()))

for index, (key, value) in enumerate(city.items()):
    print(index, key, value)
    ws.write(index, 0, key)
    ws.write(index, 1, value)

wb.save('city.xls')
file.close()
