from optparse import OptionParser
import locale
from gsmmodem.modem import GsmModem
import logging


PORT = '/dev/modem0'
BAUDRATE = 115200
PIN = None # SIM card PIN (if any)

if __name__ == '__main__':

    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE)
    modem.smsTextMode = True
    modem.connect(PIN)
    sms = "hello"

    modem.sendSms(+79227814419, sms)

    try:
        modem.rxThread.join(100)  # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    finally:
        modem.close();