#!/usr/bin/env python3

import math

x = 1.0
while x < 10.0:
    print(x, '\t', math.log(x) / math.log(2.0))
    x += 1.0
    #x = x * 2.0  # para encontrar os logaritmos de  outras potencias de dois

print('Done!')