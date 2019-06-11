# i=100
# try:
#     10/(i-100)
# except Exception as e:
#     print(e)
# finally:
#     print("执行完毕")

class MySelfException(Exception):
    def __init__(self,lenght,atlest):
        self.lenght=lenght;
        self.atlest=atlest;
def main():
    while(1):
        s=input("请输入")
        try:
            if(len(s)<3):
                raise MySelfException(len(s),3)
        except MySelfException as result:
            if result.lenght==3:
                print("MySelfException:输出的长度%d,长度至少为%d" %(result.lenght,result.atlest))
            else:
                raise MySelfException(result.lenght,3)


main()