import json

# json中dumps表示将Python对象（字典，列表等）转化为json字符串,s表示string
# dump表示将转化后的内容写进文件

person = {"name": "wuchao", "age": 30, "tel": ["1123334", "1323435"], "isonly": True}
# person = ["1123334", "1323435"]
print(person)
print(type(person))

#转换为json格式
dict2json = json.dumps(person
                       , indent=4 #分割符，表转化输出
                       , sort_keys=True #是否排序
                       )
print(dict2json)
print(type(dict2json))

# 写入文件
dict2jsonfile = json.dump(person
                          , open('demo.json', "w")
                          , indent=4
                          , sort_keys=True)

# json格式转化为python对象

#转换为python对象格式
demo = '{"age": 30, "isonly": true, "name": "wuchao", "tel": ["1123334", "1323435"]}'
json2dict = json.loads(demo)
print(json2dict)
print(type(json2dict))

#读取json文件，输出为python对象

jsonfile2dict = json.load(open("demo.json", "r"))
print(jsonfile2dict)
print(type(jsonfile2dict))