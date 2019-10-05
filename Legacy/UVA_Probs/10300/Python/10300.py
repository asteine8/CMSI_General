import sys
import re

lines = sys.stdin.readlines()[2:]
burden = 0

for line in lines:
    if (len(re.findall(r'[ ]+', line)) > 0):
        stats = list(map(lambda x: int(x), line.split(' ')))
        burden += stats[0] * stats[2] if (stats[1] > 0) else 0
    else:
        print(burden)
        burden = 0
print(burden)