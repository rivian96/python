#!/usr/bin/python3

import socket  

#yaha pe ham define kr rhe hai ki ipv4 (socket.AF_INET)
# ka use kr rhe h with tcp(socket.SOCK_STREAM)

s=socket.socket(socket.AF_INET , socket.SOCK_STREAM)

# s.setsockopt(socket.SOL_SOCKET, optname, value)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


s.bind(("127.0.0.1",8888)) 

print("listening....")

s.listen(1)

client, addr= s.accept()  #s.accept hamein do cheezein return krta hai 
					 # first is client jisko ham send kr sakte h
					 #aur recieve kr sakte hai
					 # aur ham kissey connected hai uski ip
					 #and port bhi batata hai
print("connected")

while True:
	cmd = input("$ ")
	client.send((cmd).encode())
	if cmd == "exit":
		break 
	output = (client.recv(1024)).decode()
	print(output)
socket.close(0)
client.close()
