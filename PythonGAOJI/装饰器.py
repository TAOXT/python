def test1(func):
   # print("正在等待……")
    def inner():
        if False:
            func()
        else:
            print("-----没有权限-----")
        func()
    return inner

#在这里就开始进行装饰了
@test1
def f1():
    print("-----f1------")
@test1
def f2():
    print("------f2------")
# innerfunc=test1(f1)
# innerfunc()
# innerfunc=test1(f2)
# innerfunc()
#在f1调用之前就开始进行装饰了。
f1()
f2()
