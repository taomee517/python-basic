# python3 支持unicode字符集 容量：2**16 = 65536,
# 可以兼容世界所有的字符

# 两个相关的内置函数：
# ord,可以将字符转化成unicode码
# chr,可以把unicode码转成对应的字符
a = ord("A")
print(a)

b = ord("0")
print(b)

c = ord("罗")
print(c)

d = chr(c)
print(d)

# blank
e = ''
lengthOfE = len(e)
print(lengthOfE)

note = "I'm Nick!"
print(note)

text = "Hello,World!"
print(text)

# python中不能字符串加数字
print(text + note)

# 不换行的打印,end= anything
print(text,end=" ")
print(note,end='')
print("bye",end="~")
print()

val = str(3.15)
print(val)

hexVal = hex(255)
print("255转成16进制字符串：", hexVal)

text = text.replace("W","w")
print(text)