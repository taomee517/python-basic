# 解决IDE不能识别自己写的module:
# 1.打开File--> Setting—> 打开 Console下的Python Console，把选项（Add source roots to PYTHONPAT）点击勾选上
# 2.右键点击自己的工作空间文件夹，找到Mark Directory as 选择Source Root

from module1 import self_intro
import time
import random

self_intro("Nick")

# 数字的格式化输出，参考文档：https://www.runoob.com/python/att-string-format.html
print("当前UTC时间：{:.0f}".format(time.time()))

num = 76
print("{0} 转化为二进制的值是：{1:b}".format(num, num))
print("{0} 转化为16进制的值是：{1:x}".format(num, num))


x = random.randint(0, 100)
print("随机生成一个0~100的整数：{}".format(x))
