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
	connection.send('Answer the riddles three, and the flag you will see.\n')
	connection.send('Riddle 1:\n')
	connection.send('Do you want to hear a riddle?\n')
	connection.send('I would love to hear a riddle\n')
	connection.send('I am going to tellyou a riddle\n')
	connection.send('I am waiting for the riddle\n')
	connection.send('Who Am I? \n')

	data = connection.recv(256)
	if data:
		print (data)
		if data == 'TCP\n':
			connection.send('Correct!\n')
		else:
			connection.send('LOL. no.')

	else:
		print ('no more data')
		connection.close()

	connection.send('Riddle 2:\n')
	connection.send('I am going to tellyou a riddle\n')
	connection.send('Do you want to hear a riddle?\n')
	connection.send('Here comes the Ridd-\n')
	connection.send('Who Am I? \n')



	data = connection.recv(256)
	if data:
		print (data)
		if data == 'UDP\n':
			connection.send('Correct\n')
		else:
			connection.send('LOL. no.')
			
	else:
		print ('no more data')
		connection.close()

	connection.send('Riddle 2:\n')
	connection.send('I am a computer brand\n')
	connection.send('I am also OSI layer 2\n')
	connection.send('Who Am I? \n')



	data = connection.recv(256)
	if data:
		print (data)
		if data == 'MAC\n':
			connection.send('Correct! The flag is flag{n3tw0rk5_4r3_fun}\n')
		else:
			connection.send('LOL. no.')
			
	else:
		print ('no more data')
		connection.close()