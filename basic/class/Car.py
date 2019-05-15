
class Car(object):
    def __init__(self, brand):
        self.brand = brand


# python的属性可以动态的添加，和java不一样
benz = Car("Benz")
benz.plateNumber = "渝BKM435"
benz.color = "white"
# __dict__魔法方法可以获取对象的所有属性
print(benz.__dict__)
