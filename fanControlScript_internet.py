#!/bin/env python3

import os
import json

MIN_FAN = 5
MAX_FAN = 100

MIN_TEMP = 50 # fans at min at this temp
MAX_TEMP = 80 # fans at max at this temp

TEMP_POW = 3 # decrease for cooler server, increase for quiter

def get_temp():
    sensors = json.loads(os.popen('/usr/bin/sensors -j').read())
    temp0 = sensors["coretemp-isa-0000"]["Package id 0"]["temp1_input"]
    temp1 = sensors["coretemp-isa-0001"]["Package id 1"]["temp1_input"]
    return max(temp0, temp1)
'''
def determine_fan_level(temp):
    x = min(1, max(0, (temp - MIN_TEMP) / (MAX_TEMP - MIN_TEMP)))
    return int(min(MAX_FAN, max(MIN_FAN, pow(x, TEMP_POW)*(MAX_FAN-MIN_FAN) + MIN_FAN)))
'''


def set_fan(fan_level):
    '''
        0 turn the fan off
    
        1 set low speed
    
        2 set high speed
        '''
    cmd = "i8kfan 1 1"
    if(get_temp() > 50):
        cmd = "i8kfan 1 2"
    os.system(cmd)

temp = get_temp()
#fan = determine_fan_level(temp)
#temp = max(temp0,temp1)
#cmd = "echo temp >> tem.log"
#os.system(cmd)
print("temp", temp, "fan", fan)
set_fan(fan)
