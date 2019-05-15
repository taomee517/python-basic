# 定义对象描述
# __init__ 初始化对象方法
# setColor 对象的方法


class Student():
    def __init__(self, school):
        self.school = school

    def setSchool(self, school):
        self.school = school


# 实例化对象
stu = Student("重庆大学")
print(stu.school)
print(stu.__str__())



