#!/usr/bin/python
import re

def parse(input_str):
    day = check_none( re.search('[^0-9]*([0-9]+)[Dd]', input_str))
    hour = check_none( re.search('[^0-9]*([0-9]+)[Hh]', input_str))
    minute = check_none( re.search('[^0-9]*([0-9]+)[Mm]', input_str))
    second = check_none( re.search('[^0-9]*([0-9]+)[Ss]', input_str))
    return (( day * 24 + hour ) * 60 + minute ) * 60 + second

def check_none(m):
    if m == None:
        return 0
    return int(m.group(1))

