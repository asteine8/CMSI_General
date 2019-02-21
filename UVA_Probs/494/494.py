import sys
import re

inputFile = open("494.in","r")
outputFile = open("494.out","w")

lines = "".join(sys.stdin.readlines())
text = inputFile.readlines()

numWords = []

for line in text:
    # re.sub(r'[ ]+',' ', line)
    line = re.sub(r'[^a-zA-Z]', ' ', line)
    line = re.sub(r'\s+',' ', line)
    if (re.match(r'\s', line[0])):
        line = line[1:]
    if (re.match(r'\s', line[-1])):
        line = line[:-1]
    print(line)
    numWords.append(str(len(re.findall(r'[ ]+' , line)) + 1))

outputFile.write("\n".join(numWords) + "\n")
