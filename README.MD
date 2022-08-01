## fanControl is application control fanspeed for my Dell latitude

My problems is take for 5 months since I install and use Ubunu as main OS. In BIOS I select boot use EFFI (like that) and see computer freeze when I use quite 30 minutes
At first I think fan is error, but when I open and check fan still run, but it may stop immidiaty even when CPU hot (and computer freeze)

Problem solve with 2 utility:

- Install lm-sensors to get return of temp and cpu speed
- Install i8kutil to control speed fan (keep i8kutil run as service)

In Dell latitude have 3 state of speed:
- state 0: fan not spin
- State 1: fan run normal ( around 400 rpm )
- State 2: fan run strong (around (7000 rpm)

In this program, I check CPU temp, if it not run, change to state 1. if it over 60, change fan_speed to state 2. If it below 45, back to state 1.

Then Keep program run in Crontab for every 5 minute:

In terminal, run crontab -e. Select 1 (use nano to edit)
add line: 
*/5 * * * * /usr/bin/python3 /directory/to/folder/fanControl.py

Save and check it again at crontab -l

Simple

I took it here if next time intall new OS. :) 