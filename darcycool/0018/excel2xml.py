# -*- coding: utf-8 -*-
# 第 0018 题： 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中
import xlrd
from collections import OrderedDict
import json

import xml.etree.cElementTree as ET

wb = xlrd.open_workbook('city.xls')
sheet = wb.sheet_by_index(0)
number_of_row = sheet.nrows
number_of_col = sheet.ncols

city = OrderedDict()

for row in range(number_of_row):
    city[sheet.cell(row, 0).value] = sheet.cell(row, 1).value

print(city)
json_str = json.dumps(city, ensure_ascii=False, indent=4)
print(json_str)

root = ET.Element('root')
cities = ET.SubElement(root, 'citys')

cities.text = json_str

tree = ET.ElementTree(root)
tree.write('city.xml', encoding='utf8', xml_declaration=True)
