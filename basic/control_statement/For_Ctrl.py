# 从数组中遍历
for looper in (0,10):
    print(looper)

# 从范围中遍历
for it in range(10):
    if it < 9:
        print(it, end=" ")
    else:
        print(it)

# 列表生成式
powList = [x * x for x in range(10)]
for loop in powList:
    print(loop, end=" ")
