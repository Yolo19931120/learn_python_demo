import sys

print(sys.version) # 版本号
print(sys.path) # 路径
print(sys.maxsize) #可容纳的最大int
print(sys.platform) #平台
print(sys.copyright) #版权
print(sys.argv) #参数
print(sys.getdefaultencoding()) #编码
print(sys.getfilesystemencoding()) #文件编码
print(sys.getrecursionlimit()) #最大递归深度
sys.setrecursionlimit(100) #设置最大递归深度
print(sys.getrecursionlimit()) #最大递归深度

sys.exit(0) #退出程序，里面的数字表示状态码
