#!/usr/bin/env bash

#Declare and edit your parameters here
X=0
Y=1

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
python pythoncode.py "$X" "$Y"
