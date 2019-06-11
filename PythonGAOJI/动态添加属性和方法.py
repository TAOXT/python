import types
class Person:
    def __init__(self):
        self.name="we"
    def eat(self):
        print("吃苹果")
def dink(self):
    print("喝水")
@staticmethod
def play():
    print("玩手机")
@classmethod
def test(cls):
    print("测试")

p1=Person();
print(p1.name)
Person.eat="ss"
print(p1.eat)
p1.dink=types.MethodType(dink,p1)
p1.dink()
Person.play=play
Person.play()
Person.test=test
Person.test()