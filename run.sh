#!/bin/sh

if [ $# != 2 ]
then
    echo "Usage: ./run.sh <input_scans> <output_odometry>"
    exit 1
fi

# Convert laser_scans.dat to carmen format
# Convert carmen format to json
# Do scan matching
# Generate odometry
./our_to_carmen.py $1 | ./sm/carmen2json | ./sm/sm2 | ./estimations_to_odom.py $2

# Draw a pdf
#./sm/log2pdf -in laser_scans_matched.json
