import sys
import re
import math

lines = sys.stdin.readlines()[1:]

for line in lines:
    args = list(map(int, re.split(r'[ ]+', line.strip())))

    print(round(math.ceil((args[0]-2)/3) * math.ceil((args[1]-2)/3)))
