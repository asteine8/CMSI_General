import sys
import re

TICKS_PER_ROTATION = 40
DEGREES_PER_TICK = 360/40 # 9 degrees

lines = sys.stdin.readlines()[:-1]

def DegreesTurned(start, end, dir, rots):
    degrees = 360 * rots # base # of rotations
    if dir == 1: # Clockwise
        degrees += ( start - end if (start >= end) else start - end + TICKS_PER_ROTATION) * DEGREES_PER_TICK
    else: # CCW
        degrees += ( end + TICKS_PER_ROTATION - start if (start > end) else end - start) * DEGREES_PER_TICK
    return degrees

for line in lines:
    args = list(map(int, re.split(r'[ ]+', line.strip())))

    comboDegrees = DegreesTurned(args[0], args[1], 1, 2)

    comboDegrees += DegreesTurned(args[1], args[2], 0, 1)

    comboDegrees += DegreesTurned(args[2], args[3], 1, 0)

    print(round(comboDegrees))
    

