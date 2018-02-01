import serial
import time

PORT = '/dev/modem0'
BAUDRATE = 115200
PIN = "0000" # SIM card PIN (if any)

def readPort(ser):
    while ser.inWaiting():
        print(ser.read())
    ser.close()

ser = serial.Serial(port='/dev/modem0', baudrate=115200, timeout=3)



ser.write('AT\r')
time.sleep(3)
readPort(ser)

ser.write('AT+CFUN=1')
time.sleep(3)
readPort(ser)

ser.write('AT+CPIN=0000')
time.sleep(3)
readPort(ser)

ser.write('AT+CMGS=+79227814419')
time.sleep(3)

ser.write('it is work/u001A')


def readPort():
    while ser.inWaiting():
        print(ser.read())
    ser.close()