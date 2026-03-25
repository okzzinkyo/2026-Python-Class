import time
now = time.localtime()
print("현재 시각: %d시입니다."%(now.tm_hour))
print("현재 시각: %d:%d"%(now.tm_hour, now.tm_min))


print(time.asctime())