# -*- coding:utf-8 -*-

"""
作者：吴超
邮箱：1364245724@qq.com
时间：2021-03-28 17:59:12
脚本描述：

xxx.ini文件格式：

[sections]
options = values


"""

import configparser

cf = configparser.ConfigParser()
cf.read('db.ini')
# 获取sections
print(cf.sections())
# 根据sections获取options
print(cf.options('bitbucket.org'))
print(cf.options('topsecret.server.com'))
# 根据sections获取（options,values）元组
print(cf.items('bitbucket.org'))
print(cf.items('topsecret.server.com'))
# 获取values的值
print(cf.get('topsecret.server.com',"forwardx11"))
# 修改value
cf.set('topsecret.server.com',"forwardx11","no")
print(cf.get('topsecret.server.com',"forwardx11"))

# w+ 表示文件内容替换 ，修改配置文件
with open('db.ini','w+') as f:
    cf.write(f)




