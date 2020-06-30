#!/bin/bash

#This copies python files from the code directory to
#the directory specified by the SIMULATOR_DIRECTORY
#environment variable. The first argument, if present,
#specifies the file to use as robot.py. All python
#files in the simulator directory are deleted

rm $SIMULATOR_DIRECTORY/*.py
cp *.py $SIMULATOR_DIRECTORY
if [ "$#" -ge 1 ]; then
    echo "Using $1 as robot.py"
    mv $SIMULATOR_DIRECTORY/$1 $SIMULATOR_DIRECTORY/robot.py
fi
