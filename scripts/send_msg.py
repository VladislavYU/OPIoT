#!/usr/bin/python
# -*- coding: utf-8 -*-

import locale
from optparse import OptionParser

from modemGSM.ModemGSM import ModemGSM

parser = OptionParser()
parser.add_option("-a", "--address", action="store", dest="ip", type="string", help="Cureent ip address")


if __name__ == '__main__':
    encode = locale.getdefaultlocale()
    (options, args) = parser.parse_args()


    print (modem)

    if options.ip is None:
        parser.print_help()
        exit()

    modem = ModemGSM()
    modem.send_msg('+79227814419',options.ip)

    try:
        modem.rxThread.join(100)  # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    finally:
        modem.close();