import win32api
import time
import win32con

# First key then value dict format###
Characters_Dict = {
	1 : "Left Mouse Button Click", 2 : "Right Mouse Button Click", 3 : "", 4 : "Mouse Scroll Button Click", 5 : "5", 6 : "6", 7 : "7", 8 : "Backspace", 9 : "TAB", 10 : "10", 11 : "11", 12 : "12", 13 : "Enter", 14 : "14",
	15 : "15", 16 : "Shift", 17 : "CTRL", 18 : "ALT", 19 : "Pause Break", 20 : "Capslock", 21 : "21", 22 : "22", 23 : "23", 24 : "24", 25 : "25", 26 : "26", 27 : "Escape",
	28 : "28", 29 : "29", 30 : "30", 31 : "31", 32 : "", 33 : "Page Up", 34 : "Page Down", 35 : "End", 36 : "Home", 37 : "Left Arrow Key", 38 : "Up Arrow Key", 39 : "Right Arrow Key", 40 : "Down Arrow Key",
	41 : "41", 42 : "42", 43 : "", 44 : "PRT SC",45 : "INS", 46 : "DEL", 47 : "47", 48 : "0", 49 : "1", 50 : "2", 51 : "3", 52 : "4", 53 : "5", 54 : "6",
	55 : "7", 56 : "8", 57 : "9", 58 : "58", 59 : "59", 60 : "60", 61 : "61", 62 : "62", 63 : "63", 64 : "64", 65 : "A", 66 : "B", 67 : "C", 68 : "D",
	69 : "E", 70 : "F", 71 : "G", 72 : "H", 73 : "I", 74 : "J", 75 : "K", 76 : "L", 77 : "M", 78 : "N", 79 : "O", 80 : "P", 81 : "Q", 82 : "R",
	83 : "S", 84 : "T", 85 : "U", 86 : "V", 87 : "W", 88 : "X", 89 : "Y", 90 : "Z", 91 : "Windows Button", 92 : "92", 93 : "93", 94 : "94", 95 : "95", 96 : "NUMLOCK 0", 97 : "NUMLOCK 1", 98 : "NUMLOCK 2", 99 : "NUMLOCK 3", 100 : "NUMLOCK 4", 101 : "NUMLOCK 5", 102 : "NUMLOCK 6", 103 : "NUMLOCK 7", 104 : "NUMLOCK 8", 105 : "NUMLOCK 9",
	112 : "F1",113 : "F2",114 : "F3",115 : "F4", 116 : "F5", 117 : "F6", 118 : "F7", 119 : "F8", 120 : "F9", 121 : "F10", 122 : "F11", 123 : "F13"
}




keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.'@#!$/\\":
    keyList.append(char)

def key_check():
    keys = []
    for value,key in Characters_Dict.items():
    	if win32api.GetAsyncKeyState(value):
            keys.append(key)

    return keys


#print(win32con.VK_TAB)
#for b in a:
#	if "VK" in b:
#		print(ord(b))
