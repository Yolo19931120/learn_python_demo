import time

print(time.time())
print(time.localtime())
print(time.localtime().tm_year)
print(time.localtime()[1])
print(time.ctime())
print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time() - 3600)))
# time.sleep(5)
print(time.strftime("%Y/%m/%d %H:%M:%S"))
