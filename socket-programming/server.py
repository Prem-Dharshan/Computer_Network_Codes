from datetime import datetime
import socket

# Create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()
port = 9994

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

while True:
    # Establish a connection
    clientsocket, addr = serversocket.accept()
    print(f"Got a connection from {str(addr)}")

    # Get current time
    currentTime = datetime.now() + "\r\n"

    # Send current time to client
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
