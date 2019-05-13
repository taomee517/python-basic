# for循环的优化策略：
# 1 尽量不要在循环内做不必要的计算
# 2 尽量使用局部变量，查询较快
# 3 连接多个字符串，尽量用join不要用+
# 4 列表的插入和删除尽量在末尾进行

import time

s1 = time.time()
for i in range(1000):
    list1 = []
    for j in range(10000):
        list1.append(i*5 + j*10)
e1 = time.time()
print("方法一耗时：{0} 秒".format(e1-s1))

s2 = time.time()
for i in range(1000):
    list2 = []
    c = i * 5
    for j in range(10000):
        list2.append(c + j*10)
e2 = time.time()
print("方法二耗时：{0} 秒".format(e2-s2))