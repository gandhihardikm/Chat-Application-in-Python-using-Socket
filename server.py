import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8080

#create an INET, STREAMing socket
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serversocket.bind((TCP_IP,TCP_PORT))

serversocket.listen(1)
print 'Listening....'
connection, clientaddr = serversocket.accept()
print 'Connected to : ', clientaddr

while 1:
	data = connection.recv(1024)
	print 'Client message: ', data
	print 'Enter your message: '
	server_msg=raw_input()
	connection.send(server_msg)
	if server_msg == "Bye": 
		break
	
connection.close()

