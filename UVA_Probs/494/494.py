import re

inputFile = open("494.in","r")
outputFile = open("494.out","w")

text = inputFile.readlines()

numWords = []

for l in text:
    # re.sub(r'[ ]+',' ', l)
    l = re.sub(r'[^a-zA-Z]', ' ', l)
    l = re.sub(r'\s+',' ', l)
    if (re.match(r'\s', l[0])):
        l = l[1:]
    if (re.match(r'\s', l[-1])):
        l = l[:-1]
    print(l)
    numWords.append(str(len(re.findall(r'[ ]+' , l)) + 1))

outputFile.write("\n".join(numWords) + "\n")
