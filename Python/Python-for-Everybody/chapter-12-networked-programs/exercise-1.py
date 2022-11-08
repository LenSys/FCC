# Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it 
# can read any web page. You can use split('/') to break the URL into its component parts 
# so you can extract the host name for the socket connect call. Add error checking using 
# try and except to handle the condition where the user enters an improperly formatted or 
# non-existent URL.
# (see https://books.trinket.io/pfe/12-network.html)

import socket

url = input("Enter url: ")
try:
    if len(url) == 0:
        url = "http://data.pr4e.org/romeo.txt"
    componentParts = url.split("/")

    protocol = componentParts[0]
    hostname = componentParts[2]
except:
    print("Invalid url!")
    exit()


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
mysock.send(('GET ' + url + ' HTTP/1.0\r\n\r\n').encode())

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()