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
index = text.find("W")
print(text)
print("'W'在", text, "中的索引是：", index)
tao = "*tao*"
print(tao.strip("*"))

# python中不能字符串加数字
print(text + note)

# 不换行的打印,end= anything
print(text, end=" ")
print(note, end='')
print("bye", end="~")
print()

val = str(3.15)
print(val)

hexVal = hex(255)
print("255转成16进制字符串：", hexVal)

text = text.replace("W", "w")
print(text)

for c in note:
    print(c, end="_")
print()

# 字符串的驻留机制
# 1.字符串只在编译时进行驻留，而非运行时;
# 2.字符串长度为0和1时，默认都采用了驻留机制;
# 3.字符串被sys.intern() 指定驻留
# == 只比较值
# is 比较的是对象，需要值相等且引用一致
k = "abc"
m = "dd"
print(k + m is "abcdd")
print(k + m == "abcdd")

x = "ab" + "c"
y = "abc"
print(x is y)

x = "hello!"
y = "hello!"
print(x is y)

# 字符串的格式化
year = "2019"
month = "05"
day = "10"
hour = "21"
minute = "30"
second = "00"
pattern = "{0}-{1}-{2} {3}:{4}:{5}"
dateTime = pattern.format(year, month, day, hour, minute, second)
print(dateTime)

# {0:0<8}
# 第一个0代表占位符的下标
# 第二个0代表填充字符
# < 代表原字符串左对齐
# > ^ 代表右对齐和居中
# 8 代表最后字符串的长度
binStr = "0101"
lPattern = "转为八位的二进制字符串,并左对齐：{0:0<8}"
rPattern = "转为八位的二进制字符串,并右对齐：{0:0>8}"
lBinStr = lPattern.format(binStr)
rBinStr = rPattern.format(binStr)
print(lBinStr)
print(rBinStr)

val = 3
dPattern = "{:0>4d}"
valStr = dPattern.format(val)
print(valStr)

pi = 3.1415926
fPattern = "{:.2f}"
piStr = fPattern.format(pi)
print(piStr)

levelcode = "1/3/20/"
level = levelcode.count("/", 0, len(levelcode))
print(level)


