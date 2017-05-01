#!/usr/bin/python

from __future__ import print_function
import datetime
import time
import signal

def get_length_bin_string(bin, length):
    stripped = bin.lstrip("0b")
    return stripped.rjust(length, "0")
    

def get_hex_time(date=datetime.datetime.now()):
    sec = get_length_bin_string(bin(date.second), 6)
    min = get_length_bin_string(bin(date.minute), 6)
    min_sec = min + sec
    min_sec_hex = hex(int(min_sec, 2)).lstrip("0x").upper()
    hr = get_length_bin_string(bin(date.hour), 2)
    hr_hex = hex(int(hr, 2)).lstrip("0x").upper()
    return "%s : %s" % (hr_hex, min_sec_hex)

def handler(*args):
    exit(0)

if __name__ == "__main__":
    #print(get_hex_time(datetime.datetime(2017,4,30,19,31,52)))
    signal.signal(signal.SIGINT, handler)
    print(get_hex_time(datetime.datetime.now()))
