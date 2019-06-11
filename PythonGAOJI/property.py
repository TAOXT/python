class Test:
    def __init__(self):
        self.__num=100;
    def setter(self,Num):
        self.__num=Num;
    def getter(self):
        return self.__num;
    num=property(getter,setter)

t=Test()
t.num=50#在这里实设置属性
print(t.num)#在这是返回属性值
#相当于对方法进行了封装

