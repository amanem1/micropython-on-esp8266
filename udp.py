#UDP SERVER
import socket
call = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#declaring its udp datagram
call.bind(('127.0.0.1',12345)) # setting local hostandportno.
#sending data and receiving data 

while 1:
    data,addr=call.recvfrom(4096)#we have to also receive the adress so to send data back as its a  connection less
    message=("hello iam  aman ").encode('utf-8')
    call.sendto(message,addr)
    
 -============================================================================================================================================================================================================================================================================================================================================================================================================================================================    
#udp client 
import socket
client_socket=socket.socket(AF_INET,socket.SOCK_DGRAM)
msg="hello iam amans server"
client_socket.sendto(msg.encode("uft-8"),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(4096)
print("server says ")
print(str(data,'utf8'),end='')
client_socket.close()
