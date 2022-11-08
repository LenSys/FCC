# Exercise 2: Change your socket program so that it counts the number of characters 
# it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of 
# characters and display the count of the number of characters at the end of the 
# document.
# (see https://books.trinket.io/pfe/12-network.html)

import socket

url = input("Enter url: ")
try:
    if len(url) == 0:
        url = "http://data.pr4e.org/romeo.txt"
    componentParts = url.split("/")

    hostname = componentParts[2]
except:
    print("Invalid url!")
    exit()


import socket

fileData = ""
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((hostname, 80))
mysock.send(('GET ' + url + ' HTTP/1.0\r\n\r\n').encode())

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    # print(data.decode())
    fileData = fileData + data.decode()
mysock.close()

print(fileData[:3001])
print(len(fileData), "characters")