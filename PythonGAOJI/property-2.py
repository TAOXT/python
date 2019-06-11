class Test:
    def __init__(self):
        self.__num=100;

    @property
    def num(self):
        return self.__num;

    @num.setter#如果在这里要这样使用的话，@num.setter必须要在property下面
    def num(self, Num):
        self.__num = Num;

t=Test()
t.num=50#在这里实设置属性
print(t.num)#在这是返回属性值
#相当于对方法进行了封装

