#!/bin/bash

pkill -f "python3 app.py"

cd ~/Desktop/ScanStation

python3 app.py &

sleep 7

firefox-esr http://localhost:5000 &


