# -*- coding:utf-8 -*-

"""
作者：吴超
邮箱：1364245724@qq.com
时间：2021-03-28 14:05:21
脚本描述：

"""

a = {1,2,3}
print(a)
b = list(a)
print(b)
c = tuple(i for i in b)
print(c)
d = set(b)
print(d)