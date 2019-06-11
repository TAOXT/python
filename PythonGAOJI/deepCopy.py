import copy

a=[11,222,333]
b=a
print(id(a))
print(id(b))
print(a is b)
a.append(44)
print(a)
#print(b)

c=a
b=copy.deepcopy(a)
a.append(33)
print(id(a))
print(id(b))
print(a)
print(b)
a.append(44)
print(b)
print(c)
#在这看深拷贝和浅拷贝的不同
#浅拷贝是只是把地址拷过去，内容没有考，当被拷贝的对象内容改变时，他也会随之改变
#深拷贝是把内容拷过去，当被拷贝内容改变时，他不会随之改变。


#浅拷贝
c=[a,b]
e=copy.copy(c)
print(e)
a.append(77)
print(c[0])
print(e[0])


c=(a,b)
e=copy.copy(c)
print(id(c))
print(id(e))
#这一块就是浅拷贝，为什么不同于前面的列表的拷贝呢，因为在这是元组是不可循环，而列表是循环的
#而相对于拷贝来说的时候，列表只拷贝一层，而元组的来说一层都不考虑。


