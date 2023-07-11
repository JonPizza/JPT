import socket

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('localhost', 5050))

s2.send(b'Start!')
s2.close()