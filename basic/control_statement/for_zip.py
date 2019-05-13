# for + zip 可实现并行循环

org = ("fuzik", "auto", "panda")
gdp = ("3.26亿", "1.08亿", "17.88亿")

for org, gdp in zip(org, gdp):
    print("{0} 工业总产值：{1}".format(org, gdp))

