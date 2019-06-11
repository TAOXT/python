from socket import*

udpSocket=socket(AF_INET,SOCK_DGRAM)
udpSocket.bind("",7788)
recvData=udpSocket.recv(1024)
#可以将接收到的数据分开，把发送方的信息和数据分开
#如果是想将发送的信息输出，要进行解压用decode\

content,info=recvData
print("content is %s" %content.decode("gb2312"))

print(recvData)