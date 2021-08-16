# -*- coding: utf-8 -*-
"""
@Time : 2021/8/14 11:29
@Author : 华大大不是大大
@File : study01.py
"""
import keyword

print('开始学习python基础课程')

# python关键字
kwlist = keyword.kwlist
print(kwlist)
print("关键字总共有{0}个".format(len(kwlist)))


# for i in range(1, 9):
#     print(i * "*")


def tables_99():
    """
    九九乘法表
    :return:
    """
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print("{0}*{1}={2}".format(i, j, i * j), end=' ')
        print()


with open('file.txt', 'r') as f:
    f.read()
