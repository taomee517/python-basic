# 列表的创建
a = list()
b = []
c = range(10)
d = list("abc")

print(a)
print(b)
print(list(c))
print(d)

# 元素的增加
print(id(a))
a.append("A")
print(a)
print(id(a))

print("--------------------")
print(id(a))
a.extend(["B", "M"])
print(a)
print(id(a))

# 地址发生改变，中间进行了数组拷贝，重新生成了新的对象
print("--------------------")
print(id(a))
a = a + ["K"]
print(a)
print(id(a))

print("--------------------")
print(id(a))
a.insert(3, "Z")
print(a)
print(id(a))

# 列表元素的删除
b = list("ABCDEF")
print(b)
b.pop()
print(b)
b.remove("D")
print(b)

# 列表的切片
print(list(c[:]))
print(list(c[1:]))
print(list(c[0::2]))
print(list(c[1::2]))
print(list(c[10:5:-1]))


t = tuple()
t = (10, 20, 30)
print(t)
print(type(t))

t = 10,
print(t)
print(type(t))
