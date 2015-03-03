import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))
print 'Server Connected.'
while 1:
	print 'Enter your message: '
	client_msg=raw_input()
	
	s.send(client_msg)
	data=s.recv(1024)
	print 'Server Message: ',data
	if client_msg == "Bye" :
		break
	
s.close()


