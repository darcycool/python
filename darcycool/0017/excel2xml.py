# -*- coding: utf-8 -*-
# 第 0017 题： 将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中
import json
import xml.etree.cElementTree as ET
from collections import OrderedDict
from xml.dom import minidom

import xlrd

root = ET.Element("root")
student = ET.SubElement(root, "students")

wb = xlrd.open_workbook('student.xls')
sheet = wb.sheet_by_index(0)
number_of_rows = sheet.nrows
number_of_columns = sheet.ncols

student_dict = OrderedDict()

for row in range(number_of_rows):
    items = [sheet.cell(row, col).value for col in range(1, number_of_columns)]
    student_dict[sheet.cell(row, 0).value] = items
print(student_dict)

json_str = json.dumps(student_dict, ensure_ascii=False, indent=4)
print(json_str)

student.text = json_str

tree = ET.ElementTree(root)
tree.write('student.xml', encoding='utf-8', xml_declaration=True)

xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml()
with open('student1.xml', 'w') as f:
    f.write(xmlstr)
