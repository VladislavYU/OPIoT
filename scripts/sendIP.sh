#!/bin/bash

ip=$hostname -I

python ./home/orangepi/OPIoT/scripts/send_msg.py -a $ip