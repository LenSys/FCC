# Retrieve image over HTTP
# (see https://books.trinket.io/pfe/12-network.html)

import socket
import time

HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(5120)
    if (len(data) < 1): break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

# Look for the end of the header (2 CRLF)
pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

# Skip past the header and save the picture data
picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()

# Code: http://www.py4e.com/code3/urljpeg.py

# When the program runs it produces the following output:
# 
# $ python http-retrieve-image.py
# 2920 2920
# 1460 4380
# 1460 5840
# 1460 7300
# ...
# 1460 62780
# 1460 64240
# 2920 67160
# 1460 68620
# 1681 70301
# Header length 240
# HTTP/1.1 200 OK
# Date: Sat, 02 Nov 2013 02:15:07 GMT
# Server: Apache
# Last-Modified: Sat, 02 Nov 2013 02:01:26 GMT
# ETag: "19c141-111a9-4ea280f8354b8"
# Accept-Ranges: bytes
# Content-Length: 70057
# Connection: close
# Content-Type: image/jpeg

# You can see that for this url, the Content-Type header indicates that body of the document 
# is an image (image/jpeg). Once the program completes, you can view the image data by 
# opening the file stuff.jpg in an image viewer.
