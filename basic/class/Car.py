
class Car(object):
    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def show_property(cls):
        print("百公里加速时间：5s")

    def get_color(self):
        return self.color


# python的属性可以动态的添加，和java不一样
benz = Car("Benz")
benz.plateNumber = "渝BKM435"
benz.color = "white"

# __dict__魔法方法可以获取对象的所有属性
print(benz.__dict__)

# 方法上加注解@classmethod，且方法的形参为cls代表静态方法
Car.show_property()
print(benz.get_color())
