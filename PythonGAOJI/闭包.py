# def test(number):
#     print("-----------")
#     def test_in(number_in):
#         return number+number_in
#     return number
#
# a=test(12)
# print(a)


def test(a,b):
    print("%d,%d" %(a,b))
    def test_in(x):
        return a*x+b
    return test_in



f=test(10,2)
print(f(3))
print(f(6))