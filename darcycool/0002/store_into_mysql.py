# -*- coding: utf-8 -*-
# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import random
import string

import pymysql


def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_activation_code(size=200, len=20):
    activation_code = set()
    for i in range(size):
        activation_code.add(id_generator(len))
    return activation_code


conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       passwd='1234',
                       db='darcy')
cursor = conn.cursor()
sql = 'insert into activation_code (code) VALUE (%s)'

try:
    cursor.executemany(sql, get_activation_code())
except Exception as e:
    print('执行Mysql: %s时出错： % s' % (sql, e))
finally:
    cursor.close()
    conn.commit()
    conn.close()
