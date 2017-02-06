#!/bin/sh


# Convert laser_scans.dat to carmen format
./our_to_carmen.py

# Convert carmen format to json
./sm/carmen2json < ./laser_scans.carmen > laser_scans.json

# Do scan matching
./sm/sm2 < ./laser_scans.json > laser_scans_matched.json

# Draw a pdf
./sm/log2pdf -in laser_scans_matched.json

# Generate odometry
./matched_to_odom.py
