class Test:
    def __init__(self):
        self.__num=100;
        self._num1=200;
    def setNum(self,num):
        self.__num=num;
    def getNum(self):
        return self.__num;

t=Test();
print(t.getNum())
print(t._num1)
#前置双下划线私有变量，外部不可以访问
#前置单下划线私有变量，类的对象和子类可以访问









