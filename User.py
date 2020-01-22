from datetime import date
from datetime import datetime
import sys
import time
import socket
import pickle
import cv2
import numpy as np
HeaderSize = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('IP Address',PORT))


Record_array = []
while True:
    try:
        start_time = time.time()
        full_msg = b''
        msg_len = 0
        new_msg = True
        while True:
            msg = s.recv(4096)
            if new_msg:
                s.send(bytes("Message Received","utf-8"))
                msg_len = msg[:HeaderSize]
                new_msg = False
            full_msg += msg
            if len(full_msg)-HeaderSize == int(msg_len):
                new_msg = True
                d = pickle.loads(full_msg[HeaderSize:])
                image = d[0]
                keys = d[1]
                break 
        if keys != []:
            print(keys)
        Record_array.append([image,keys])

        #image = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
        cv2.imshow('',image)
        cv2.waitKey(2)
    except KeyboardInterrupt:
        current_time = datetime.now().time()
        np.save(f"{str(date.today())}__{str(round(time.time()-start_time,3))}.npy",Record_array)
        sys.exit("KeyboardInterrupted Exiting.....")
    except Exception as e:
        print(str(e))
        sys.exit("Exiting.....")
