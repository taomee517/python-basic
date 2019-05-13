print("请输入你的成绩：")
score = input()
score = int(score)

if score < 0 or score > 100:
    print("输入错误，成绩不合法")
elif 0 <= score < 60:
    print("不及格")
elif 60 <= score < 80:
    print("良好")
elif 80 <= score <= 100:
    print("优秀")

