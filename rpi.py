from gpiozero import LED

import socket

import sys

IP = 'frp.xsourse.cc'

port = 9997
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pin_pick = LED(6)
pin_pick.off()
pin_exist = LED(5)
pin_exist.off()
try:

    s.connect((IP,port))

except Exception as e:

    print('server not find or not open')

    sys.exit()

while True:

    #trigger = raw_input("send:")

    #s.sendall(trigger.encode())

    data = s.recv(1024)

    data = data.decode()

    print('recieved:',data)

    #if trigger.lower() == '1':

      #  break
    if data == "existfar":
        pin_exist.on()
    elif data == "noball":
        pin_exist.off()
    if data == "existpick":
        pin_pick.on()
    elif data == "far":
        pin_pick.off()

s.close()


