import sys
import re
from collections import Counter

lines = sys.stdin.readlines()[1:]
affairs = []

for line in lines:
    line = re.sub(r'[ ]+', ' ', line) # Remove duplicate spaces
    if (line[0] == " "): # Remove starting space if present
        line = line[1:]
    args = re.split(r'[ ]+',line, 1) # Split country and name

    affairs.append(args[0])

affairs.sort()
affairDict = list(Counter(affairs).items())

for item in affairDict:
    print("{} {}".format(item[0], str(item[1])))