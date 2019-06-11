num=100
def test():
    num=200
    def inner():
        num=300
        print(num)
    return inner

ret=test()
ret()
#作用域就是先查看局部变量，如果局部变量中没有，查找闭包，如果这个没有查找全局变量，如果全局变量中没有则查看我认为是python自带的