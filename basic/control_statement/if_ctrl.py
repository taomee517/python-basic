# False, 0, 0.0, 空值None, 空序列对象(空的列表, 元组, 集合, 字典, 字符串), 空range, 空迭代都是 False

if False:
    print(False)

if 0:
    print("if表达式中，认为0也是False")

if 3:
    print("if表达式中，认为非0就是True")

if 5/2:
    print("if表达式中，认为非0就是True")

a = list()

if a:
    print("if表达式中，认为空列表就是False")

a.append("OK")
if a:
    print("if表达式中，认为非空列表是True")

b = "False"
if b:
    print("if表达式中，认为非空字符串是True")