## fanControl is application control fanspeed for my Dell latitude

My problems is take for 5 months since I install and use Ubuntu as main OS. In BIOS I select boot use EFFI (like that) and see computer freeze when I use quite 30 minutes
At first I think fan is error, but when I open and check fan still run, but it may stop immidiaty even when CPU hot (and computer freeze)

Problem solve with 3 utility:

- Install lm-sensors to get return of temp and cpu speed
- Install i8kutil to control speed fan (keep i8kutil run as service)
- Install dell-bios-fan-control (git clone, copy to usr/bin and run under root every reboot computer)

```
git clone https://github.com/TomFreudenberg/dell-bios-fan-control.git

cd dell-bios-fan-control

make dell-bios-fan-control

chmod + x dell-bios-fan-control

cp dell-bios-fan-control /usr/bin/

```
add to crontab: 

`@reboot dell-bios-fan-control 0
`

In Dell latitude have 3 state of speed:
- state 0: fan not spin
- State 1: fan run normal ( around 400 rpm )
- State 2: fan run strong (around (7000 rpm)

In this program, I check CPU temp, if it not run, change to state 1. if it over 60, change fan_speed to state 2. If it below 45, back to state 1.

Then Keep program run in Crontab for every 5 minute:

In terminal, run crontab -e. Select 1 (use nano to edit)
add line: 
*/5 * * * * /usr/bin/python3 /directory/to/folder/fanControl.py (or write to my_script.sh and run script)

Save and check it again at crontab -l

Simple

I took it here if next time intall new OS. :) 

# Update
15/09/2022: Write newControl.py that allow program run every 15 seconds and start program at restart. 1 minutes is too long heat can rise quick and freeze CPU
