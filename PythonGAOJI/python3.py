#
# a=[11,22,33]
# b=[11,22,33]
# print(a==b)
# print(a is b)
# c=a
# print(c==b)
# print(c==a)
# print(c is a)
# print (c is b)
# print(id(a))
# print(id(b))
# print(id(c)) #这个赋值是因为在程序中赋值是另一个变量的引用，也就是指向同一个地址
# #==是判断值的内容是否相等，is是判断地址是否相等。

a=100
b=100
print(a is b)
#在这里是因为在整数的中把-128~255看做的是一个数组，里面是内容，而这里面都是a,b,都是数组的引用。

