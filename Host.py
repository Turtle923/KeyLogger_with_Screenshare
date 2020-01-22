import socket
import time
import cv2
import numpy as np
import pickle
from PIL import ImageGrab
from getkeys import key_check
#img = cv2.imread('1112.jpg')

def key_to_output(keys):
    output = [0]*81

    if 'A' in keys:
        output[0] = 1
    elif 'B' in keys:
        output[1] = 1
    elif 'C' in keys:
        output[2] = 1
    elif 'D' in keys:
        output[3] = 1
    elif 'E' in keys:
        output[4] = 1
    elif 'F' in keys:
        output[5] = 1
    elif 'G' in keys:
        output[6] = 1
    elif 'H' in keys:
        output[7] = 1
    elif 'I' in keys:
        output[8] = 1
    elif 'J' in keys:
        output[9] = 1
    elif 'K' in keys:
        output[10] = 1
    elif 'L' in keys:
        output[11] = 1
    elif 'M' in keys:
        output[12] = 1
    elif 'N' in keys:
        output[13] = 1
    elif 'O' in keys:
        output[14] = 1
    elif 'P' in keys:
        output[15] = 1
    elif 'Q' in keys:
        output[16] = 1
    elif 'R' in keys:
        output[17] = 1
    elif 'S' in keys:
        output[18] = 1
    elif 'T' in keys:
        output[19] = 1
    elif 'U' in keys:
        output[20] = 1
    elif 'V' in keys:
        output[21] = 1
    elif 'W' in keys:
        output[22] = 1
    elif 'X' in keys:
        output[23] = 1
    elif 'Y' in keys:
        output[24] = 1
    elif 'Z' in keys:
        output[25] = 1
    elif ' ' in keys:
        output[26] = 1
    elif '1' in keys:
        output[27] = 1
    elif '2' in keys:
        output[28] = 1
    elif '3' in keys:
        output[29] = 1
    elif '4' in keys:
        output[30] = 1
    elif '5' in keys:
        output[31] = 1
    elif '6' in keys:
        output[32] = 1
    elif '7' in keys:
        output[33] = 1
    elif '8' in keys:
        output[34] = 1
    elif '9' in keys:
        output[35] = 1
    elif '0' in keys:
        output[36] = 1
    elif 'F1' in keys:
        output[37] = 1
    elif 'F2' in keys:
        output[38] = 1
    elif "F3" in keys:
        output[39] = 1
    elif 'F4' in keys:
        output[40] = 1
    elif 'F5' in keys:
        output[41] = 1
    elif 'F6' in keys:
        output[42] = 1
    elif 'F7' in keys:
        output[43] = 1
    elif 'F8' in keys:
        output[44] = 1
    elif 'F9' in keys:
        output[45] = 1
    elif 'F10' in keys:
        output[46] = 1
    elif 'NUMLOCK 1' in keys:
        output[47] = 1
    elif 'NUMLOCK 2' in keys:
        output[48] = 1
    elif 'NUMLOCK 3' in keys:
        output[49] = 1
    elif 'NUMLOCK 4' in keys:
        output[50] = 1
    elif 'NUMLOCK 5' in keys:
        output[51] = 1
    elif 'NUMLOCK 6' in keys:
        output[52] = 1
    elif 'NUMLOCK 7' in keys:
        output[53] = 1
    elif 'NUMLOCK 8' in keys:
        output[54] = 1
    elif 'NUMLOCK 9' in keys:
        output[55] = 1
    elif 'NUMLOCK 0' in keys:
        output[56] = 1
    elif 'Page Down' in keys:
        output[57] = 1
    elif 'Page Up' in keys:
        output[58] = 1
    elif 'End' in keys:
        output[59] = 1
    elif 'Home' in keys:
        output[60] = 1
    elif 'Left Arrow Key' in keys:
        output[61] = 1
    elif 'Up Arrow Key' in keys:
        output[62] = 1
    elif 'Right Arrow Key' in keys:
        output[63] = 1
    elif 'Down Arrow Key' in keys:
        output[64] = 1
    elif 'PRT SC' in keys:
        output[65] = 1
    elif 'INS' in keys:
        output[66] = 1
    elif 'DEL' in keys:
        output[67] = 1
    elif 'Left Mouse Button Click' in keys:
        output[68] = 1
    elif 'Right Mouse Button Click' in keys:
        output[69] = 1
    elif 'Mouse Scroll Button Click' in keys:
        output[70] = 1
    elif 'Backspace' in keys:
        output[71] = 1
    elif 'TAB' in keys:
        output[72] = 1
    elif 'Enter' in keys:
        output[73] = 1
    elif 'Shift' in keys:
        output[74] = 1
    elif 'CTRL' in keys:
        output[75] = 1
    elif 'ALT' in keys:
        output[76] = 1
    elif 'Pause Break' in keys:
        output[77] = 1
    elif 'Capslock' in keys:
        output[78] = 1
    elif 'Escape' in keys:
        output[79] = 1
    elif 'Windows Button' in keys:
        output[80] = 1

    # print(output)
    return output







HeaderSize = 10
HostName = socket.gethostname()
print(HostName)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((IP Address,Port))
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
        ni = cv2.cvtColor(ni,cv2.COLOR_BGR2GRAY)
        keys = key_check()
        output = (key_to_output(keys))
        msg = pickle.dumps((ni,output))
        msg = bytes(f'{len(msg):<{HeaderSize}}',"utf-8") + msg 

        clientSocket.send(msg)




