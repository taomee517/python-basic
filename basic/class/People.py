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
    def __init__(self):
        self.field = "IT"


p = People()
m = Man("张飞")
pro = Programmer()
pro.position = "project manager"
print(p.__dict__)
print(m.__dict__)
print(m.__doc__)
print(pro.__dict__)
print(pro.sex)
pro.work()
