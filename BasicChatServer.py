import socket
import sys

comms_socket = socket.socket()
host = ''
port = 9999
comms_socket.bind((host, port))
comms_socket.listen(10)
connection, address = comms_socket.accept()

while True:
	print(address[0] + ": " +connection.recv(4096).decode("UTF-8"))
	print("")
	send_data = input("Reply: ")
	connection.send(bytes(send_data, "UTF-8"))
	print("")