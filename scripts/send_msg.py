#!/usr/bin/python
# -*- coding: utf-8 -*-

from optparse import OptionParser
import locale
from gsmmodem.modem import GsmModem
import logging

parser = OptionParser()
parser.add_option("-a", "--address", action="store", dest="ip", type="string", help="Cureent ip address")

PORT = '/dev/modem0'
BAUDRATE = 115200
PIN = "0000" # SIM card PIN (if any)

if __name__ == '__main__':
    encode = locale.getdefaultlocale()
    (options, args) = parser.parse_args()
    if options.ip is None:
        parser.print_help()
        exit()

    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE)
    modem.smsTextMode = True
    modem.connect(PIN)

    modem.sendSms(+79227814419, options.ip)

    try:
        modem.rxThread.join(10)  # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    finally:
        modem.close();