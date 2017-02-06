#!/usr/bin/env python3


with open("laser_scans.dat") as f:
    lines = f.readlines()

with open("laser_scans.carmen", 'w') as f:
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

        f.write(out + "\n")
