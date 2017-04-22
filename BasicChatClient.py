import socket

comms_socket = socket.socket()
host = '192.168.1.84'
port = 9999
comms_socket.connect((host, port))

while True:
	send_data = input("Message: ")
	comms_socket.send(bytes(send_data, "UTF-8"))
	print(comms_socket.recv(4096).decode("UTF-8"))
