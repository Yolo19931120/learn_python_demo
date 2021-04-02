
# %[-.+,m,.n,0](d,s,f,x,o)
# %表示占位符
# [-.+,m,.n,0]表示
# -，+ 表示左右对齐；m 表示输出的宽度； .n 表示保留几位小数，或者字符串取前几位；0表示剩余宽度用0填充
# [d,s,f,x,o] 表示格式符
# d数字，s字符串，f浮点数，x十六进制，o八进制

name = "wuchao"
age = 30
salary = -19234.6753

#format形式，变量只能用key:value传递
print("我叫{name}，年龄：{age}，收入：{salary}".format(name="wuchao",age=30,salary=19234.6753))
#f的形式可以读取上文的变量，直接引用。其他语法完全和format一直
print(f"我叫|{name:+^10.4s}|， 年龄：|{age}|，收入：|{salary:<20,.2f}|")
