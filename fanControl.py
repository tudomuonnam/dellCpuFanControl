#!/usr/bin/python3


import json
import os,subprocess

from datetime import datetime

MAX_LINES = 5000

TEMP_MAX_SPEED = 60
TEMP_MIN_SPEED = 45

def get_status():

    cmd = '/usr/bin/sensors -j'
    output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    sensors = json.loads(output.communicate()[0])
    #sensors = json.loads(os.popen('/usr/bin/sensors -j').read())
    cpu_fan = sensors["dell_smm-isa-0000"]["fan1"]["fan1_input"]

    temp0 = sensors["coretemp-isa-0000"]["Core 0"]["temp2_input"]
    temp1 = sensors["coretemp-isa-0000"]["Core 1"]["temp3_input"]

    temp = max(temp0, temp1)
    return(cpu_fan,temp)

def fan_control(cpu_fan,temp):
    #cpu_fan,temp = get_status()

    cmd = "i8kfan - -"
    status = "keep status"
    # Fan khong hoat dong: kich hoat fan
    if (cpu_fan < 1000): 
        cmd = "i8kfan 1 1"
        status = "start fan"
    # Nhiet do > 50 va fan hoat dong cham: tang toc fan
    if (temp > TEMP_MAX_SPEED and cpu_fan < 4500): 
        cmd = "i8kfan 1 2"
        status = "fan in max speed"
    if ( temp < TEMP_MIN_SPEED and cpu_fan > 5000):
        cmd = "i8kfan 1 1"
        status = "reduce fan speed"
    os.system(cmd)
    return(status)
def log_file(cpu_fan,temp,status):
    # write logfile
    now_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    log = "Time: {}, temp: {}, cpu_fan: {}, status: {} \n".format(now_string, temp,cpu_fan,status)
    print(log)
    with open("fan_control.log", 'a') as f:
        f.write(log)
def truncate_logfile(max_lines):
    #delete logfile if it have more than 5,000 line
    lines = sum(1 for line in open('fan_control.log'))
    if(lines > max_lines):
        file = open("fan_control.log","r+")
        file.truncate(0)
        file.close()

cpu_fan,temp = get_status()
status = fan_control(cpu_fan,temp)
log_file(cpu_fan,temp,status)
truncate_logfile(MAX_LINES)
