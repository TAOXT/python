#定义函数
def print_menu():
    print('*'*50)
    print("1,xx")
    print("1,xx")
    print("1,xx")
    print("1,xx")
    print("*"*50)
def Print_Dayin():
    i=1
    while i<=5:
        j=1
        while j<=i:
            print("*",end=(""))
            #end()传递一个参数，表示不换行
            j+=1
        print("")
        i+=1

def Print_Duo(*t):
    print("可变参数为：")
    for x in range(len(t)):
        print(t[x])

    print("可变参数的长度为：")
    print(len(t))
def RetanceL():
    i=1
    sum=0
    for i in range(1,101):
        if i%2==1:
            continue
        sum+=1
    print(sum)
def Print_List(List):
    for i in range(len(List)):
        print(List[i],end=" ")

list=[1,2,3,4,5]
Print_List(list)
Print_Duo(1,2,4,5)

