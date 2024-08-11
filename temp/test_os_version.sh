#!/bin/bash
RESULT=$(cat /etc/os-release)
echo $RESULT
if [[$RESULT == *"40 (Workstation Edition)"]]
then echo "True"
else echo "False"
fi
if [[ $RESULT == *"40 (Workstation Edition)"* && $RESULT == *"Fedora Linux"* && $? == 0 ]];
then echo "SUCCESS"
else echo "FAIL"
fi
