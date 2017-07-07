# -*- coding: utf-8 -*-
# 第 0003 题： 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
import random
import string
import redis


def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_activation_code(size=200, len=20):
    activation_code = set()
    for i in range(size):
        activation_code.add(id_generator(len))
    return activation_code


def save_codes(codes):
    r = redis.Redis(host='127.0.0.1',
                    port=6379,
                    db=0)
    pipeline = r.pipeline()
    for c in codes:
        pipeline.sadd('code', c)
    pipeline.execute()
    return r.scard('code')


save_codes(get_activation_code(200, 20))
