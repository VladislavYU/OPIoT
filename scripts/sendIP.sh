#!/bin/bash

hostName -I > $ip

python ./home/orangepi/OPIoT/scripts/send_msg.py -a $ip