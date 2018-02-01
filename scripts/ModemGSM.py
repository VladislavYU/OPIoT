import serial
import time

class ModemGSM:

    PORT = '/dev/modem0'
    BAUDRATE = 115200
    PIN = "0000"  # SIM card PIN (if any)

    def __init__(self):
        self.ser = serial.Serial(port=self.PORT, baudrate=self.BAUDRATE, timeout=3)


    def readPort(self):
        while self.ser.inWaiting():
            print(self.ser.read())

    def connect(self):
        self.ser.write('AT\r')
        time.sleep(3)

        self.ser.write('AT+CFUN=1\r')
        time.sleep(5)

        self.ser.write('AT+CPIN=0000\r')
        time.sleep(3)

        self.ser.write('AT+CMGF=1\r')
        time.sleep(3)



    def send_msg(self, phone, text):
        self.ser.write('AT+CMGS='+text+'\r')
        time.sleep(3)

        self.ser.write(text+'\x1a')
        time.sleep(3)


