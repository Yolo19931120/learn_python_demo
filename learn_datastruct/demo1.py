# -*- coding:utf-8 -*-

"""
作者：吴超
邮箱：1364245724@qq.com
时间：2021-03-28 13:07:54
脚本描述：python数据结构demo
list,tuple,str,dict等
"""
import  logging
logging.basicConfig(level=logging.DEBUG
                    ,format="%(asctime)s - %(filename)s - %(lineno)s - %(message)s"
                    ,datefmt="%Y-%m-%d %H:%M:%S")


l1 = ["a", 1, "b", 2, "c", 3]

def print_item(l1):
    for i, item in enumerate(l1):
        logging.info(f'{i}:{item}')
    logging.info("=="*20)

print_item(l1)

del l1[0]
print_item(l1)

l1.pop(2)
print_item(l1)

l1.pop()
print_item(l1)

l1.insert(3,10)
print_item(l1)

try:
    l1.remove("f")
except Exception as e:
    logging.exception(e)
print_item(l1)



