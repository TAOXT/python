# a=3
# b=4
# print(a+b)
# print(a*b)
# print(a/b)#this ineuqalitf otherc++orjava this is daily math
# print(a//b)#取整
# print(a**b) #取幂次



#列表
# languagelist=['c++','java','c#']
# print(languagelist[0])
# print(languagelist[2])
# print(languagelist)
# languagelist.append('python')
# print(languagelist)
#
# langu1=['c']
# langu1.extend(languagelist)
# print(langu1)
#
# for i in range(len(langu1)):
#     print(langu1[i])
#
# for index,value in enumerate(langu1):
#     print("第%d个元素是%s"%(index,value))


# #定义多维表
# list=[['3','4'],['12'],['c']]
# for i in range(len(list)):
#     print(list[i])
#
# for i in range(len(list)):
#     list1=list[i]
#     for j in range(len(list1)):
#         print(list1[j])



# #元组
# t=('1',2,5.6)
# print(t)
# for index ,value in enumerate(t):
#     print("第%d个元素是%s"%(index,value))


# l=list(t)
# l.sort()
# #在这里会报错，因为在进行排序的时候，将元组转换为列表的时候，然后进行排序，必须是同一类型的对象
# t=tuple(l)
# print(t);

#字典
#d={'name':'小童','sex':'女','age':'19'}
# print(d)
# print(d['name'])
# print(d['sex'])
# print(d['age'])

#再添加键值的时候若不存在则添加，如果存在则修改
# d['collage']='nankai'
# d['age']=18
# print(d)

# d2={'name':'小童','inde':10,'age':19}
# d.update(d2)
#合并两个字典,是合并不相同的
# print(d)

#删除字典元素
# d.pop('name')
# print(d)
#
# if 'age' in d:
#     print(d['age'])
# else:
#     print("不存在这个索引")

# for key in d.keys():
#     print('键'+key+'的值：'+d[key]);

# for value in d.values():
#     print( value);


# d={'name':{'first':'小童','next':'lee'},'sex':'女','age':'19'}
# print(d['name']['next'])

#集合
#可变集合和不可变集合
s=set('python')
print(type(s))
print(s)

#不可变
fs=frozenset('python')
print(type(fs))
print(fs)

for e in fs:
    print(e)
