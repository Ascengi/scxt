#!/system/xbin/bash
green='\033[32;1m'
red='\033[31;1m'
sleep 2
echo $green
python pfgk.py
echo "masuk..."
echo $red
python logo.py
sleep 3
echo $green
python system.py
echo "bye tuan.."