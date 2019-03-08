#!/usr/bin/env bash

#Declare and edit your parameters here
radiousA=5
radiousB=100
path="/home/clemente/hub/Datasets/PA_Datasets/pirate_data.csv"

#Just some code to build suspance
printf "Welcome \n"
sleep 1

echo "Your parameters will be loaded soon:"

echo -ne '#####                     (33%)\r'
sleep 2
echo -ne '#############             (66%)\r'
sleep 2
echo -ne '#######################   (100%)\r'

#Pass your parameter to the main pythoncode file
python Main.py "$radiousA" "$radiousB" "$path"
