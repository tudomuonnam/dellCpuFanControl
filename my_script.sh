#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
python3 newControl.py


sleep 30 && xrandr --output eDP-1 --brightness 0.8
