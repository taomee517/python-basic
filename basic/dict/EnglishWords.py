words = dict()
words.__setitem__("你慘了", "your goose will be cooked!")
words.__setitem__("古代先贤", "ancient sages")


keys = words.keys()
for key in keys:
    print('请用英语说：' + key)
    value = words.get(key)
    index = 0
    while True:
        result = input()
        if result == value:
            print("恭喜你，答对了！")
            break
        else:
            if index == 2:
                print("不好意思，你已经连续三次答错了！正确答案是：" + value)
                break
            else:
                print("不对哦！请再想想，输入正确答案!")
            index += 1
