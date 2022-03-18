import socket
# http://data.pr4e.org/romeo.txt
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input("Enter url - ")
host = url.split("/")[2]
mysock.connect((host, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  print(data.decode())
mysock.close()