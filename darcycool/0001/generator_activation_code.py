# -*- coding: utf-8 -*-
# 第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import string
import random


def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_activation_code(size=200):
    activation_code = set()
    for i in range(size):
        activation_code.add(id_generator())
    return activation_code

print(get_activation_code())
