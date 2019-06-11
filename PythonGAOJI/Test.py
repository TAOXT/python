def func(funcName):
    print("-------func1-------")
    def inner(*args,**kwargs):
        print("-----g1----")
        funcName(*args,**kwargs)
        print("------g2----")
    print("-------func2--------")
    return inner
@func
def test1(a,b,c):
    print("a=%d,b=%d,c=%d" %(a,b,c))
@func
def test2(a,b,c,d):
    print("a=%d,b=%d,c=%d,d=%d" %(a,b,c,d))

test1(10,11,12)
test2(10,11,12,13)

