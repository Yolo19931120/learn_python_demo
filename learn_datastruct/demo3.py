# -*- coding:utf-8 -*-

"""
作者：吴超
邮箱：1364245724@qq.com
时间：2021-03-28 14:12:22
脚本描述：

"""
list1 = [("wuchao",30), ("yami",90), ("shenzheng",70), ("china",50)]

dict1 ={x:y for x,y in list1}
print(dict1)

print(dict1.setdefault('guangdong',100))
print(dict1)

print(dict1.get('wuchao',None))
print(dict1)

for i in dict1:
    print(i)

list2 = [("qinghai",30), ("hubei",90), ("sichuan",70), ("china",1000)]
dict1.update(list2)
print(dict1)
