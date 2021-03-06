import math
import numpy as np

import sys
sys.path.append('../')

import constants as const
import conversions as conv

# B = uNI
# N = B/uI

L = 1.3
D = conv.cm_to_m(2.92)
I = 18
B = conv.unmilli(24.3)

N = B * L / (const.u_0 * I)

circum = math.pi * D

L = N * circum

print(L)
