
# class Person:
#     def SayHello(self):
#         print("hello")
# p=Person()
# p.SayHello();

# class MyString:
#     str=""
#     def __init__(self):
#         self.str="Mysting"
#     def output(self):
#         print(self.str)
#
# s=MyString()
# s.output()


# class UserInfo:
#     username=""
#     _pwd=""
#     def __init__(self,name,pwd):
#         self.username=name
#         self._pwd=pwd;
#     def output(self):
#         print(" user:"+self.username+"\npassword:"+self._pwd)
#     def __del__(self):
#         print("byebye~")
# u=UserInfo("ADMIN","123456")
# u.output();


# class Users(object):
#     s=''
#     online_count=0
#     def __init__(self):
#         Users.online_count+=1
#         self.s="ccc"
#     @staticmethod#静态方法
#     def staticmd():
#         print("staticmethod")
#     @classmethod
#     def classcmd(cls):
#         print("第%d个元素是%s" % (cls.online_count, cls.s))#classmethod cont visit 实例变量
#     def __del__(self):
#         Users.online_count-=1
# a=Users();
# a.staticmd()
# a.online_count+=1
# a.classcmd()
# print(isinstance(a,Users))#use isinstance pan duan shi fou shi zhe ge lei
# print(Users.online_count)


#继承
# import time
# class Users:
#     username = ""
#     def __init__(self, name):
#        self.username=name
#        print("构造函数%s"%self.username)
#     def disUserName(self):
#         print(self.username)
# class UserLogin(Users):
#     lastLoginTime=""
#     def __init__(self,uname,lastLoginTime):
#         # 调用父类的构造函数
#         Users.__init__(self,uname)
#
#         self.lastLoginTime=lastLoginTime
#     def disLoginTime(self):
#         print("登录的时间为："+self.lastLoginTime)
#
# #获取当前的时间
# now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#
# #声明3的对象
# myUser_1=UserLogin('admin',now)
# myUser_2=UserLogin('admin',now)
# myUser_3=UserLogin('admin',now)
#
# #分别调用父类和子类的函数
# myUser_1.disUserName()
# myUser_1.disLoginTime()
# myUser_2.disUserName()
# myUser_2.disLoginTime()
# myUser_3.disUserName()
# myUser_3.disLoginTime()

#抽象类和多态
#定义抽象类要通过导入ABCMeta类和abstractmethod
from abc import ABCMeta,abstractmethod
class myabc(object):
    __metaclass__=ABCMeta
    @abstractmethod
    def absmethod(self):pass
class Shape(object):
    __metaclass__=ABCMeta
    def __init__(self):
        self.color="black"
    @abstractmethod
    def draw(self): pass
    def toString(self):
        print("woshi%s" %(str(Shape)));

class cricl(Shape):
    x=y=r=0
    def __init__(self,x,y,r):
        self.x=x;
        self.y=y;
        self.r=r;
    def draw(self):
        print("Draw Cricle:(%d,%d,%d)"%(self.x,self.y,self.r))
    def toString(self):
        print("woshi%s" %(str(cricl)));
class line(Shape):
    x=y=x2=y2=0
    def __init__(self,x,y,x2,y2):
        self.x=x;
        self.y=y;
        self.x2=x2;
        self.y2=y2;
    def draw(self):
        print("Draw line:(%d,%d,%d,%d)"%(self.x,self.y,self.x2,self.y2))
    def toString(self):
        super().toString()#实现方法被重写
        print("woshi%s" %(str(line)));
c=cricl(10,10,5)
c.draw()
l=line(10,10,20,20)
l.draw()
l.toString()


