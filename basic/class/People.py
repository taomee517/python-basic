class People:
    def __init__(self):
        self.self = self


# 双引号用于docString,三引号用于代码内的doc
'Man：中文称这为男人'


class Man(People):
    """Man：中文称之为男人"""
    sex = "male"
    sex_cn = "男人"

    def __init__(self, name):
        self.name = name

    def work(self):
        print("{0} ，就得努力工作，赚钱养家！".format(self.sex_cn))


class Programmer(Man):
    field = "IT"

    def __init__(self, name):
        Man.__init__(self, name)


p = People()
m = Man("张飞")
pro = Programmer("小王")
pro.position = "project manager"
print(p.__dict__)
print(m.__dict__)
print(m.__doc__)
# 自有属性
print(pro.__dict__)

# 全部属性，包括父类
print(dir(pro))
print(pro.sex)
pro.work()
