def fun():
    a,b=0,1
    for x in range(10):
        print(b)
        yield b
        #在这里表示yield是将值存储到一个生成器
        a,b=b,a+b
a=fun()
# for x in a:
#     print(x)

ret=a.__next__()
print(ret)
ret=a.__next__()
print(ret)
ret=a.__next__()
#这个每次next输出的是
print(ret)

# 当下面这条语句运行后，他会将x的值赋值为send方法的参数，并且继续执行到下一个yield

a.send("xxx")
print(a.__next__())
