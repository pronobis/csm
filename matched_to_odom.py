#!/usr/bin/env python3

import json
import math

with open("laser_scans_matched.json") as f:
    lines = f.readlines()

output = []
with open("odometry.dat", 'w') as f:
    for l in lines:
        jsn = json.loads(l)
        estimate = jsn['estimate']
        tstamp = jsn['timestamp']
        f.write("0 0 0 %d %d 2 0 6 %g %g 0 %g 0 0\n" %
                (tstamp[0], tstamp[1],
                 estimate[0], estimate[1], (estimate[2] % (2 * math.pi))))
