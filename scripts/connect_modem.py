import serial

PORT = '/dev/modem0'
BAUDRATE = 115200
PIN = "0000" # SIM card PIN (if any)


ser = serial.Serial(port='/dev/modem0', baudrate=115200, timeout=3)
ser.open()
ser.write('AT\r')


while ser.inWaiting():
    print(ser.read())
ser.close()