import sys
openQuote = True
lines = sys.stdin.readlines()
char = 0
for line in lines:
    while char < len(line):
        if line[char] == '"':
            if openQuote:
                line = line[0:char] + "``" + line[char+1:]
                openQuote = False
            else:
                line = line[0:char] + "''" + line[char+1:]
                openQuote = True
        char += 1
    line = line.replace("\n","")
    char = 0
    print(line)