# -*- coding: utf-8 -*-
"""
@Time : 2021/8/15 12:21
@Author : 华大大不是大大
@File : homework01.py
"""
import math
import random

'''
1、用print函数打印多个值
2、用print函数不换行打印
3、导入模块的方式有哪些
4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
5、python3中可以支持哪些数值类型？
6、判断变量类型有哪些方式，分别可以用哪些函数？
7、分别对49.698作如下打印
	1）四舍五入，保留两位小数
	2）向上入取整
	3）向下舍取整
	4）计算8除以5返回整型
	5）求4的2次幂
	6）返回一个（1,100）随机整数
'''

# 1、用print函数打印多个值
print('1', 1, 'a')

# 2、用print函数不换行打印
print('aaa', end='  ')
print('bbb', end='--')
print()

# 3、导入模块的方式有哪些
print('直接导入：import *')
print('设置别名导入：import * as *')
print('只导入模块中的变量、部分类或函数：from * import *')

# 4、python有哪六种数据类型？不可变数据类型有哪些？可变数据类型有哪些？
print("python的六种数据类型：string字符串类型、list列表类型、number数字类型、tuple元组类型、set集合类型、dictionary字典类型")
print("不可变的数据类型有：number类型、tuple类型、string类型")
print("可变的数据类型有：list类型、set类型、dic类型")

# 5、python3中可以支持哪些数值类型？
print("python3中可以支持哪些数值类型:int、float、bool、comple四种类型")

# 6、判断变量类型有哪些方式，分别可以用哪些函数？
print("判断变量类型有type（）和isinstance()两种类型")
a = 'a'
print(type(a))
print("判断变量a是否为str类型：", isinstance(a, str))

'''7、分别对49.698作如下打印
1）四舍五入，保留两位小数
2）向上入取整
3）向下舍取整
4）计算8除以5返回整型
5）求4的2次幂
6）返回一个（1,100）随机整数'''
x = 49.698
print("四舍五入保留两位小数：", round(x, 2))
print('向上取整：', math.ceil(x))
print("向下取整：", int(x))
print("计算8除以5返回整型", 8//5)
print("求4的2次幂", 4**2)
print('返回一个（1,100）随机整数', random.randint(1, 100))
