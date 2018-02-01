#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
from optparse import OptionParser
import serial
import time

#from modemGSM.ModemGSM import ModemGSM

parser = OptionParser()
parser.add_option("-a", "--address", action="store", dest="ip", type="string", help="Cureent ip address")


if __name__ == '__main__':
    encode = locale.getdefaultlocale()
    (options, args) = parser.parse_args()

    if options.ip is None:
        parser.print_help()
        exit()

        ser = serial.Serial(port='/dev/modem0', baudrate=115200, timeout=3)

        ser.write('AT\r')
        time.sleep(3)

        ser.write('AT+CFUN=1\r')
        time.sleep(6)

        ser.write('AT+CPIN=0000\r')
        time.sleep(3)

        ser.write('AT+CMGF=1\r')
        time.sleep(3)

        ser.write('AT+CMGS=+79227814419\r')
        time.sleep(3)

        ser.write(options.ip+'\x1a')
        time.sleep(3)
        ser.close()



    #modem = ModemGSM()
    #modem.send_msg('+79227814419',options.ip)


    #modem.close();