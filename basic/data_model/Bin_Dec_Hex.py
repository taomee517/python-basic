# 2进制，8进制，10进制，16进制

# 2进制写法，以0b(零B)开头，逢2进1，只包含0，1
x = 0b1010
print("2进制的0b1010等于：", x)

# 8进制写法，以0o(零O)开头，逢8进1，只包含0~7
y = 0o517
print("8进制的0o517等于：", y)

# 16进制写法，以0x(零X)开头，逢G进1，只包含0~F
z = 0xf8c
print("16进制的0xf8c等于：", z)


# 类型转化，字母不能直接转能整型，会报错
a = int(3.14)
print(a)

b = int("123")
print(b)

c = int(True)
print(c)

d = round(8.5)
print(d)

e = round(8.5000001)
print(e)




