from socket import*

#创建套接字
udpSocket=socket(AF_INET,SOCK_DGRAM)
#准备接受方的地址
sendData='1243'
udpSocket.sendto("hhh",('127.0.0.1',7788))#这样的是错误的，这样的话，是因为python3
#改正
udpSocket.sendto(sendData.encode("utf-8"),('127.0.0.1',7788))
