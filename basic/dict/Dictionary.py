
dictTemp = {"nickName": "taomee", "sex": "male"}

print(dictTemp)
print(dictTemp.keys())
print(dictTemp.values())

# 元素的删除
del dictTemp["sex"]
print(dictTemp)

# 元素的新增和修改
dictTemp["age"] = 30
print(dictTemp)

dictTemp["nickName"] = "jackson"
print(dictTemp)

# 根据key获取value
print(dictTemp["nickName"], end="\t")
print(dictTemp["age"])
