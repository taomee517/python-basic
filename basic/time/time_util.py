import time

utcMillis = time.time()
print(utcMillis)

utcSecond = int(utcMillis)
print(utcSecond)

utcMinute = utcSecond // 60
print(utcMinute)

utcHour = utcMinute // 60
print(utcHour)

utcDay = utcHour // 24
print(utcDay)

utcYear = utcDay // 365
print(utcYear)
