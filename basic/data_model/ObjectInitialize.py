x = y = 123
print(x)

a,b = 3,5
print("===分别赋值===")
print(a)
print(b)

a,b = b,a
print("===数值交换===")
print(a)
print(b)

# python中没有常量，可以被任意赋值
# 只能程序中通过逻辑控制
PI = 3.1415926
print(PI)
PI = 60
print(PI)

# 次方（幂）运算 **
m = 2 ** 10
print("2的10次方等于：",m)

# 除并取余
i = divmod(10,3)
print(i)

j = divmod(60,12)
print(j)


# 浮点除法，整除
ka = 5/2
print(ka)

kb = 5//2
print(kb)