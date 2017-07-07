# -*- coding: utf-8 -*-
# 第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

from PIL import Image, ImageDraw, ImageFont

dogIm = Image.open('photo.jpg')
width, high = dogIm.size
draw = ImageDraw.Draw(dogIm)
draw.text((width - 10, 0), '4', fill='red', font=ImageFont.truetype('Avenir.ttc', 10))
dogIm.save('dog.jpg')
