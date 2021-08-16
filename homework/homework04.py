# -*- coding: utf-8 -*-
"""
@Time : 2021/8/15 14:21
@Author : 华大大不是大大
@File : homework04.py
"""
import time

"""
1、任意的输入10个数字，按从大到小排序
2、"在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，通过键盘输入小男孩回答的鲜花的束数，数量不一样小女生的反应也不一样。如果鲜花数大于等于9999，打印："小女生直接晕了过去",如果在1000(包含)-9999(不包含)，打印："明天就结婚",如果在100(包含)-1000(不包含)，打印："拉拉手意思意思，有空再约！",否则：打印："你是个好人"
3、输入三角形的三条边长，判断三角形的类型。根据实际情况分别打印：不能构成三角形，一般三角形，等腰三角形，等边三角形，只要能构成三角形，则还需要计算出：周长。
4、如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
5、判断输入的用户名为admin及密码为admin则打印登录成功，否则打印用户名或密码错误，登录失败
6、判断输入的数是奇数还是偶数
7、用户输入的年份是否为闰年
8、输入两个整型变量，分别使用if结构两个中的最小值
9、打印如下结果：
1*5=5
2*10=20
3*15=45
...
10*50=500
10、本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
11、计算1900年1月1日到今天(如：2019年12月20日)相距多少天。
12、打印如下图案：
*
**
***
****
*****
13、打印如下图案：
*
***
*****
*******
*********
14、打印如下图案：
#####*
####***
###*****
##*******
#*********
15、打印如下图案：
     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
16、打印99乘法表
17、定义一个List，任意输入10个数字保存到List，然后按从小到大排序。（冒泡排序
"""


def num_array1():
    # 任意的输入10个数字，按从大到小排序
    ls01 = []
    for i in range(11):
        ls01.append(int(input("请输入数字{}：".format(i))))
        if i == 10:
            print("您输入的是个数字为：", ls01)
    ls01.sort(reverse=False)
    print("您输入的十个数字从小到大排序后为：", ls01)


def ruhua():
    """
    "在一个月黑风高的夜晚，一个小男生用自己的零花钱给小女生买了一束鲜花，小女生问小男生鲜花的数量:“这花多少束?”，
    通过键盘输入小男孩回答的鲜花的束数，数量不一样小女生的反应也不一样。如果鲜花数大于等于9999，打印："小女生直接晕了过去",
    如果在1000(包含)-9999(不包含)，打印："明天就结婚",
    如果在100(包含)-1000(不包含)，打印："拉拉手意思意思，有空再约！",
    否则：打印："你是个好人"
    """
    flower = int(input("请输入买的花的数量："))
    if flower >= 9999:
        print("如花：啊~ 我晕了")
    elif 1000 <= flower < 9999:
        print("如花:宝~ 我们明天就结婚吧。")
    elif 100 <= flower < 1000:
        print("如花：我妈妈说我们只能拉手手哦~")
    else:
        print("如花：你是个好人！")


def triangle():
    # 输入三角形的三条边长，判断三角形的类型。根据实际情况分别打印：不能构成三角形，一般三角形，等腰三角形，等边三角形，只要能构成三角形，则还需要计算出：周长。
    a = int(input("请输入三角形的边长："))
    b = int(input("请输入三角形的边长："))
    c = int(input("请输入三角形的边长："))
    if 0 < c < a + b and a + c > b > 0 and c + b > a > 0:
        if a == b == c:
            print("这是一个等边三角形")
        elif a == b or b == c or a == c:
            print("这是一个等腰三角形")
        else:
            print("这是普通三角形")
        L = a + b + c
        print("三角形的 周长为{}".format(L))
    else:
        print("无法构成三角形")


def num_array2():
    # 如果输入三个不同的数，要求比较大小并按从小到大排序输出呢？如输出：a<b<c）
    ls = []
    x1 = ls.append(int(input("请输入一个数：")))
    x2 = ls.append(int(input("请输入一个数：")))
    x3 = ls.append(int(input("请输入一个数：")))
    print("您输入的数字为：", ls)
    ls.sort(reverse=False)
    for i in ls:
        print(i, end="")
        if i == ls[-1]:
            print()
        else:
            print('<', end="")


def login():
    # 判断输入的用户名为admin及密码为admin则打印登录成功，否则打印用户名或密码错误，登录失败
    admin = input("请输入admin：")
    password = input("请输入password：")
    if admin == 'admin' and password == "admin":
        print("登录成功")
    else:
        print("登录失败")


def is_odd_even():
    # 判断输入的数是奇数还是偶数
    X = int(input("请输入一个数："))
    if X >= 0:
        if X // 2 == 0:
            print("这是一个偶数")
        else:
            print("这是一个奇数")
    else:
        print("这是负数")


def is_leap_year():
    # 用户输入的年份是否为闰年
    year = int(input("请输入年份："))
    if year % 4 == 0 or year % 400 == 0:
        print("{}年是闰年".format(year))
    else:
        print("{}年不是闰年".format(year))


def compare_Two_Numbers():
    # 输入两个整型变量，分别使用if结构两个中的最小值
    A = int(input("输入数字A："))
    B = int(input("输入数字B："))
    if A > B:
        print(B)
    elif A < B:
        print(A)
    elif A == B:
        print('两个数相等')


def guilv():
    """
    打印如下结果：
    1*5=5
    2*10=20
    3*15=45
    ...
    10*50=500
    :return:
    """
    for i in range(1, 11):
        print("{}*{}={}".format(i, 5 * i, i * 5 * i))


def annualInterestRate():
    # 本金10000元存入银行，年利率是千分之三，每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
    principal = 10000
    AnnualInterestRate = 0.003

    # 每年的利息
    def interest():
        return principal * AnnualInterestRate

    for i in range(1, 6):
        principal = principal + interest()
        print('第{}年的本金为：{}'.format(i, principal))


def now_to_1900():
    # 计算1900年1月1日到今天(如：2019年12月20日)相距多少天。
    now_date = time.strftime('%Y-%m-%d', time.localtime())
    old_data = '1970-01-02'
    old_data = time.strptime(old_data, '%Y-%m-%d')
    print("1970年的时间组：", old_data)
    print('当前时间组：', time.localtime())
    print("当前的时间戳：", time.time())
    print("1970年的时间戳：", time.mktime(old_data))
    print("当前日期距离1970-01-02的时间为：", time.time() - time.mktime(old_data))
    print("一天等于{}秒".format(60*60*24))
    print("相差的天数为", (time.time() - time.mktime(old_data))//(60*60*24))
    print("18853天大约等于", 18853//365)
    print("1970至今为", 2021-1970)


if __name__ == '__main__':
    now_to_1900()
