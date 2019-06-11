class Person:
    __slots__=("name","age")
#__slots__是用来限定属性的，如果只允许对某个类的实例添加一定个数的实例
p=Person()
p.name="老王"
p.age=40
print("老王的年龄%d" %(p.age))
