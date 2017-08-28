# -*- coding: utf-8 -*-
# 第 0019 题： 将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中
import xlrd
import xml.etree.cElementTree as ET

wb = xlrd.open_workbook('numbers.xls')
sheet = wb.sheet_by_index(0)
number_of_row = sheet.nrows
number_of_col = sheet.ncols

numbers = []

for row in range(number_of_row):
    number = [sheet.cell(row, col).value for col in range(number_of_col)]
    numbers.append(number)

print(numbers)
print(isinstance(numbers, list))
root = ET.Element('root')
numbers_element = ET.SubElement(root, 'numbers')
numbers_element.text = str(numbers)

tree = ET.ElementTree(root)
tree.write('numbers.xml', xml_declaration=True, encoding='utf-8')
