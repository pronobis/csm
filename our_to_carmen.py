#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: our_to_carmen.py <input_scans>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

for l in lines:
    l = l.split(' ')
    # Header
    nrays = int(l[2])
    out = "FLASER %s" % nrays
    # Rays
    for r in l[16:16 + nrays]:
        out += " " + r.strip()
    # Estimate and odometry
    out += " %s %s %s %s %s %s" % (0, 0, 0, 0, 0, 0)
    # Timestamp
    out += " %s 0 %s" % (l[3], l[4])

    print(out)
