import socket
s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_address= '192.168.0.130'
port= 8888
target= (ip_address,port)
s.bind(target)
while True:
    message= s.recvfrom(120)
    print(message)
    data = message[0]
    data = "\n"
    print(data.encode('ascii'))
# except Exception as e:    #exception use when any error occur
#print("i have recieved the message")