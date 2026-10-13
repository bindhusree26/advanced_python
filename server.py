import socket
# create a socket
server = socket.socket()
# using bind() assigns IP address(localhost) and port(5000)
server.bind(("localhost",5000))# addresss to connect between client and server
# since the address is ready we can send connection from server to client
#listen() waits for one client to connect
server.listen(1)
# displays waiting message
print("waiting for client...")
# receving the connection from client to server
# accept() accepts the client connection and stores clients's address
client, address = server.accept()
# message being recieved from client
# recevies up to 1024 bytes(need to call again if we need to receive more data)
print("connected to:",address)
message = client.recv(1024).decode()# decode() converts bytes to string
# displays the message received from the client
print("message from client:",message)
# sends a reply to client (b = bytes)
client.send(b"hello client")
client.close()# closes the client connection
server.close()# closes the server socket
#python "c:\Users\Student\Desktop\advancedpython\server.py"