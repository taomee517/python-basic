import random

words = dict()
words.__setitem__("你慘了", "your goose will be cooked!")
words.__setitem__("勿谓言之不预", "Don't say we didn't warn you!")
words.__setitem__("古代先贤", "ancient sages")
words.__setitem__("稀土", "rare earth")
words.__setitem__("混乱", "disorder")
words.__setitem__("制动档", "brake gear")
words.__setitem__("离合", "clutch")
words.__setitem__("妥协", "compromise")
words.__setitem__("招募", "recruit")
words.__setitem__("抗议", "protest")
words.__setitem__("算法", "algorithm")
words.__setitem__("委员会", "committee")
words.__setitem__("致命的", "fatal")
words.__setitem__("没有意义", "make no sense")
words.__setitem__("私下的", "under the table")
words.__setitem__("橡皮子弹", "rubber bullet")
words.__setitem__("潦草", "scrawl")
words.__setitem__("资本主义", "capitalism")
words.__setitem__("美联储", "the Federal Reserve")

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
