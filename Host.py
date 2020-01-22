import socket
import time
import cv2
import numpy as np
import pickle
from PIL import ImageGrab
from getkeys import key_check

HeaderSize = 10
print(socket.gethostname())
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('IP Address',PORT))
s.listen()
while True:
    clientSocket, address = s.accept()
    print(f"Connect Established from {address}")
    host,port = address
    
    while True:
        time.sleep(0.0755555)
        img = ImageGrab.grab()
        ni = np.array(img)
        ni = cv2.resize(ni,(1200,720))
        ni = cv2.cvtColor(ni,cv2.COLOR_BGR2RGB)
        ni = cv2.cvtColor(ni,cv2.COLOR_RGB2GRAY)
        keys = key_check()
        msg = pickle.dumps((ni,keys))
        msg = bytes(f'{len(msg):<{HeaderSize}}',"utf-8") + msg 

        clientSocket.send(msg)




