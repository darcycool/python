# -*- coding: utf-8 -*-
# 第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片
import random
import string

from PIL import ImageDraw, Image, ImageFont, ImageFilter


def get_code():
    return [random.choice(string.ascii_letters) for _ in range(4)]


def get_point_color():
    return (random.randint(65, 90), random.randint(65, 90), random.randint(65, 90))


def get_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def get_picture():
    width = 230
    height = 60
    # 画布
    im = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('Avenir.ttc', 40)
    draw = ImageDraw.Draw(im)
    code = get_code()

    for t in range(4):
        draw.text((60 * t + 10, 0), code[t], font=font, fill=get_color())

    # 噪点
    for _ in range(random.randint(2000, 3000)):
        draw.point((random.randint(0, width), random.randint(0, height)), fill=get_point_color())

    # 模糊
    im = im.filter(ImageFilter.BLUR)

    im.save("".join(code) + '.jpg', 'jpeg')


if __name__ == '__main__':
    get_picture()
