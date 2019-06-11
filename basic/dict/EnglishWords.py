import random

words = dict()
words.__setitem__("你慘了", "your goose will be cooked!")
words.__setitem__("古代先贤", "ancient sages")
words.__setitem__("稀土", "rare earth")


# items = words.items()

keys = list(words.keys())
random.shuffle(keys)
size = keys.__len__()
num = 0
right = 0
for key in keys:
    num += 1
    print('请回答第{}题，请用英语说：{}'.format(num, key))
    value = words.get(key)
    index = 0
    while True:
        result = input()
        if result == value:
            right += 1
            print("恭喜你，答对了！")
            break
        else:
            if index == 2:
                print("不好意思，你已经连续三次答错了！正确答案是：" + value)
                break
            else:
                print("不对哦！请再想想，输入正确答案!")
            index += 1
score = int(right/size * 100)
print("本轮测试共有{}题，你答对了{}题，你的成绩是：{}分".format(size, right, score))
