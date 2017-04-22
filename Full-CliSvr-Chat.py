import socket

def Server():
	global port
	host = ""

	comms_socket = socket.socket()
	comms_socket.bind((host, port))

	print("Waiting for a chat at LOCALHOST on port ", port)

	comms_socket.listen(10)
	send_data = ""

	while True:
		connection, address = comms_socket.accept()
		print("Opening chat with ", address)
		while send_data != "EXIT":
			recv_data = connection.recv(4096).decode("UTF-8")
			if recv_data == "EXIT":
				break
			print(address[0], ": ", recv_data)
			send_data = input("Reply: ")
			connection.send(bytes(send_data, "UTF-8"))

		print("-----Conversation Ended-----")
		send_data = ""
		connection.close()


def Client():
	global port
	print("Enter the host you want to communicate with (leave blank for localhost) ")
	host = input("> ")
	if host == "":
		host = "localhost"

	comms_socket = socket.socket()

	print("Starting a chat with ", host, "on port ", port)
	comms_socket.connect((host, port))
	send_data = ""

	while True:
		while send_data != "EXIT":
			send_data = input("Message: ")
			comms_socket.send(bytes(send_data, "UTF-8"))
			recv_data = comms_socket.recv(4096).decode("UTF-8")
			if recv_data == "EXIT":
				break
			print(host + ": " + recv_data)
			
		comms_socket.close()	
		print("-----Conversation Ended-----")

	
port = int(input("Enter the port you want to communicate on (0 for default): "))
if port == 0:
	port = 9999

while True:
	print("Your options are:")
	print("1 - Wait for a chat")
	print("2 - Initiate a chat")
	print("3 - Exit")

	option = int(input("Option: "))

	if option == 1:
		Server()
	elif option == 2:
		Client()
	elif option == 3:
		break
	else:
		print("Please enter a correct option No. ")