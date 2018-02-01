import serial
import time
from modemGSM.ModemGSM import ModemGSM

PORT = '/dev/modem0'
BAUDRATE = 115200
PIN = "0000" # SIM card PIN (if any)

def readPort(ser):
    while ser.inWaiting():
        print(ser.read())

ser = serial.Serial(port='/dev/modem0', baudrate=115200, timeout=3)



ser.write('AT\r')
time.sleep(3)
readPort(ser)

ser.write('AT+CFUN=1\r')
time.sleep(6)
readPort(ser)

ser.write('AT+CPIN=0000\r')
time.sleep(3)
readPort(ser)

ser.write('AT+CMGF=1\r')
time.sleep(3)
readPort(ser)

ser.write('AT+CMGS=+79227814419\r')
time.sleep(3)
readPort(ser)

ser.write('it is work\x1a')
time.sleep(3)
readPort(ser)

ser.close()
