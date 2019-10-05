import sys
import re

lines = sys.stdin.readlines()[1:]

for line in lines:
    args = list(map(int,re.split(r'[ ]+', line.strip())))
    if (args[0] == args[1]):
        print('=')
    elif (args[0] < args[1]):
        print('<')
    else:
        print('>')