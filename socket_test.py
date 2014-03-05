""" Tutorialspoint code. Not mine.
"""

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
s.close                     # Close the socket when done