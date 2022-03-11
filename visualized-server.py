import socket
import json
from time import sleep
import numpy as np
import matplotlib.pyplot as plot
HOST = '192.168.50.126' # IP address
PORT = 4048 # Port to listen on (use ports > 1023)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)

        while True:
            data = conn.recv(1024).decode()
            print("Received from socket server:", data)
            
            if (data.count("{") != 1):
                sleep(0.1)
                continue

            obj = json.loads(data)
            
            t = obj['s']
            plot.scatter(t, obj['acc_x'], c='blue')
            plot.scatter(t, obj['acc_y'], c='red')
            plot.scatter(t, obj['acc_z'], c='green')
            plot.scatter(t, obj['gy_x'], c='pink')
            plot.scatter(t, obj['gy_y'], c='orange')
            plot.scatter(t, obj['gy_z'], c='purple')
            plot.xlabel("sample num")
            plot.pause(0.0001)