import socket 
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	port = int(sys.argv[1])
	if (65535 < port) or (port < 1024):
		print ('Please enter a valid port1. Goodbye.')
		exit()

except:
	print ('Please enter a valid port. Goodbye.')
	exit()

ipAddress = '127.0.0.1'
server_address = (ipAddress,port)
sock.bind(server_address)

sock.listen(1)

print ('Server Running on port {} waiting...').format(port)

while True:
	connection, addr = sock.accept()
	print ('Got connection from:', addr)

	data = connection.recv(256)
	if data:
		print (data)
		if data == 'flag{y0u_say_hell0!}\n':
			connection.send('Correct: real flag is flag{and_I_say_g00dbye!}')
		else:
			connection.send('LOL. no.')
	else:
		print ('no more data')
		connection.close()
