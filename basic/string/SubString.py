from dateutil import parser

text = "abcdefg"

print("取出全部：", text[:])

print("取出2以后的：", text[2:])

print("取出0~4：", text[:4])

print("取出2~4：", text[2:4])

print("从1~6每2位取一位：", text[1:6:2])

print("取出最后两位", text[-2:])

print("逆序排列", text[::-1])

msg = "80 80 00 13 FA D6 00 D3 0D 0A"
subMsgs = msg.split()
end = subMsgs[-1]
print(end)

otuMsg = "10c,100,010,001,100,000,000,100,100,010,010,100,000,000"
abilities = otuMsg.split(",")
print("Tag = ", abilities[0])
print(abilities)

bcdTime = "190509231806"
bcdTime = "20" + bcdTime
fmtTime = parser.parse(bcdTime)
print(fmtTime)
