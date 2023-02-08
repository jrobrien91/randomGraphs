import serial
from datetime import datetime
import time
filename = input("Input Filename:") + '.txt'
file = open(filename, 'w+')


def pollsave():

    now = datetime.now()
    ser.write(b'0R0\r\n')
    data = ser.readline()
    day = now.strftime("%Y"+"%m"+"%d")
    time = now.strftime("%H:%M:%S")
    datatime = day + ',' + time + ','+ data.decode('utf-8')
    with open(filename, "a") as myfile:
        myfile.write(datatime)
    print(datatime)


with serial.Serial('COM4', 19200, timeout = 1) as ser:
    starttime = time.time()
    while True:
        pollsave()
        print(time.time())
        time.sleep(0.25 - ((time.time() - starttime) % 0.25))
