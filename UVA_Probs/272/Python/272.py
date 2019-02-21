import sys

lines = "".join(sys.stdin.readlines())

counter = 0
outputString = ""

for i in range(len(lines)):
    if (lines[i] == '"'):
        if (counter % 2 == 0):
            outputString += "``"
        else:
            outputString += "''"
        counter += 1
    else:
        outputString += lines[i]

print(outputString, end='')