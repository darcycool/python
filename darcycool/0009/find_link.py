# -*- coding: utf-8 -*-
# 第 0009 题： 一个HTML文件，找出里面的链接。

import requests
from bs4 import BeautifulSoup

url = r'https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html'
response = requests.get(url)
soup = BeautifulSoup(response.text)
for link in soup.find_all('a'):
    print(link.get('href'))
