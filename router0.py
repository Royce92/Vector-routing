from socket import *
import sys


table = {
    
    'destination0': { 'interface': "Local", 'Cost': 0},
    'destination1': {'interface': '104.238.129.39', 'Cost': 1},
    'destination2': {'interface': '104.238.130.63', 'Cost': 3},
    'destination3': {'interface': '104.238.135.148', 'Cost': 7}}

for k, v in table.items():
    interface =v["interface"]
    if interface != "Local":
        print(interface)
        s = socket(AF_INET,SOCK_STREAM)
        host = interface
        port = 50011
        s.connect((host, port))
        local_table = str(table)
        s.send(local_table.encode())
        receivedMsg = s.recv(1024).decode()
        s.close()
        print ('Client: Connection closed')
        print(receivedMsg)
        table = (receivedMsg)


