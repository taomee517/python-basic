# 从数组中遍历
for looper in (1, 2, 3):
    print(looper, end=" ")
print()

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
print()

text = "Hello,World"
for c in text:
    if "," == c:
        break
    print(c, end="_")
print()

for x in range(10, 0, -2):
    print(x, end="_")


listTemp = ["OK", "Hello", "Bye"]
print()
print(listTemp[:])

listTemp.append("Love")
print(listTemp)

