import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input("Enter url - ")
host = url.split("/")[2]
mysock.connect((host, 80))
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0
while True:
  data = mysock.recv(512)
  if (len(data) < 1):
    break
  for char in data.decode():
    count = count + 1
print(count)
mysock.close()