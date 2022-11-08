# Exercise 5: (Advanced) Change the socket program so that it only shows data after 
# the headers and a blank line have been received. Remember that recv is receiving 
# characters (newlines and all), not lines.

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

# read all data from socket url
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break

    # store file data
    fileData = fileData + data.decode()
mysock.close()

# split lines of file data
tmpFileData = fileData.split('\r\n')

ignoreLine = True
for line in tmpFileData:

    # check for empty line
    if len(line) == 0:
        # headers are finished after empty line, set ignore headers to false
        ignoreLine = False

    # ignore line if still headers
    if ignoreLine: continue

    # print line if not empty
    if len(line) != 0:
        print(line)