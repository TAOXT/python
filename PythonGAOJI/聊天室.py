from socket import*

def main():
    udpSocket=socket(AF_INET,SOCK_DGRAM)
    udpSocket.bind("",7788)
    while True:
        recvInfo=udpSocket.recv(1024)
        content,Info=recvInfo
        print("数据是%s,信息是%s" %(content,Info))

if __name__=="__main__":
    main()


