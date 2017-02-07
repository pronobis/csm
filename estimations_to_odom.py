#!/usr/bin/env python3

import json
import math
import sys

if len(sys.argv) != 2:
    print("Usage: our_to_carmen.py <output_odom_file>")
    sys.exit(1)


output = []
with open(sys.argv[1], 'w') as f:
    for l in sys.stdin:
        jsn = json.loads(l)
        estimate = jsn['estimate']
        tstamp = jsn['timestamp']
        f.write("0 0 0 %d %d 2 0 6 %g %g 0 %g 0 0\n" %
                (tstamp[0], tstamp[1],
                 estimate[0], estimate[1], (estimate[2] % (2 * math.pi))))
