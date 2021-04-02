import  random,string

def gen_random_str(length):
    # 随机生成几位整数，要留以为给字符
    numcount = random.randint(1, length - 1)
    strcount = length - numcount
    # 从string集合里获取数字和字符
    numlist = [random.choice(string.digits) for _ in range(numcount)]
    strlist = [random.choice(string.ascii_letters) for _ in range(strcount)]
    # 合在一起
    alllist = numlist + strlist
    # 打乱
    random.shuffle(alllist)
    # 列表转字符串
    result = "".join(alllist)
    return result


for i in range(10):
    random_str = gen_random_str(32)
    print(random_str)

