import random
# 随机生成一个整数
print(random.randint(1,10))
# 随机生成奇数或者偶数[a,b,m]，m表示步长，
# 例如步长是2，如果a是偶数，则取到的都是偶数，因为偶数加2都是偶数，奇数同理
print(random.randrange(0,100,2))
print(random.randrange(1,100,2))
# 随机生成浮点数
print(random.uniform(1,2))
# 随机从集合里选择一个数
ll = ["a","b","c","d"]
print(random.choice(ll))
# 随机取几个数
print(random.sample(ll, 2))
# 随机打乱
random.shuffle(ll)
print(ll)
