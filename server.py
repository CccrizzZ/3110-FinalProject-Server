import json
import sys
import random
import time
import socket
from _thread import *
import threading
from operator import itemgetter
import json
import requests
import pickle





def RunServer():

    
    serverRoom = []
    port = 12345
    ThreadCount = 0
    ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # start server
    try:
        ServerSideSocket.bind(('',port))
    except socket.error as e:
        print(str(e))

    # listen to clients
    print("waiting for clients...")
    ServerSideSocket.listen()

    # connection loop
    while True:
        Client, address = ServerSideSocket.accept()
        Client.settimeout(5)

        print("Connected to: " + address[0] + ":" + str(address[1]))

        # start new client thread
        start_new_thread(ClientConnection, (Client, ))

        ThreadCount += 1
        print("Thread number: " + str(ThreadCount))

    ServerSideSocket.close()
    

# client thread
def ClientConnection(conn):
    
    
    m = "Server is working"
    conn.send(str.encode(m))

    while True:

        # receive target client data
        data = conn.recv(1024)
        resp = '' + data.decode('utf-8')
        
        
        # if no client data, disconnect
        if not data:
            break
        
        # send to client
        conn.sendall(str.encode(resp))
        print("send to client:" + resp)

    conn.close()









if __name__ == '__main__':
    RunServer();