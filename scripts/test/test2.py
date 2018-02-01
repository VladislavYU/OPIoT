import serial
ser = serial.Serial(port='/dev/modem0', baudrate=115200, timeout=3)
ser.write("AT\r")
while ser.inWaiting():
    print(ser.read())
ser.close()