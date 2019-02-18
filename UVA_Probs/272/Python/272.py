import sys

inputFile = open("272.in","r")
outputFile = open("272.out","w")

inputString = "".join(inputFile.readlines())

counter = 0
outputString = ""

for i in range(len(inputString)):
    if (inputString[i] == '"'):
        if (counter % 2 == 0):
            outputString += "``"
        else:
            outputString += "''"
        counter += 1
    else:
        outputString += inputString[i]

# print(outputString)
outputFile.write(outputString)