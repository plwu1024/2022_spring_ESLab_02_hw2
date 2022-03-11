import socket 
import jsonimport numpy as np
import matplotlib.pyplot as plot
HOST = 'X.X.X.X'     # IP address
PORT = 6531            # Port to listen on (use ports > 1023)

data_array = []
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Starting server at: ", (HOST, PORT))
    conn, addr = s.accept()
    with conn:
        print("Connected at", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data)
            data_len = 1
            if (data.count('{') != 1):
                # Incomplete data are received.
                # Some codes here 
                # assume larger than one "{" ?
                ##############
                data_arr = data.split("}")
                for i in range(len(data_arr)):
                    data_arr[i] += "}"
                    
                ###############
            obj = json.loads(data)
            t = obj['s']plot.scatter(t, obj['x'], c='blue') 
            # x, y, z, gx, gy, gz
            # some codes here
            plot.xlabel("sample num")
            plot.pause(0.0001)