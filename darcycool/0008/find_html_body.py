# -*- coding: utf-8 -*-
# 第 0008 题： 一个HTML文件，找出里面的正文。
import requests
from bs4 import BeautifulSoup

r = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
url = requests.get(r, headers=headers)
soup = BeautifulSoup(url.text, 'html.parser')
print(soup.get_text())
