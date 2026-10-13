import socket
# create a socket
client = socket.socket()
#connects to the server using localhost and port 5000
client.connect(("localhost",5000)) # address to connect between client to server
# sends a message to the server (b = bytes)
client.send(b"hello server")# message to be passed from client to server
# recieves the server's replyand converts it to string
message = client.recv(1024).decode()
#displays the message recieved from the server
print("message from server:",message)
client.close# closes the client connection 
# python "C:\Users\Student\Desktop\advancedpython\client.py"