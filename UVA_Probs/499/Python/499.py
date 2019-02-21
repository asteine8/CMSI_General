import sys
import re
from collections import Counter

lines = sys.stdin.readlines()

for line in lines:
    line = re.sub(r'[^A-Za-z]', '', line)
    commonItems = Counter(line).most_common(len(line))
    numChars = commonItems[0][1]

    commonChars = list((char[0] for char in commonItems if char[1] == numChars))
    commonChars.sort()
    print("{} {}".format(''.join(commonChars), str(numChars)))