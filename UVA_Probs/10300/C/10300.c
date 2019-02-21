#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SIZE 124

int numCases;

int main() {

    char numCasesString[BUFFER_SIZE];
    scanf("%s", numCasesString);
    numCases = atoi(numCasesString);

    char line[BUFFER_SIZE];

    int burden = 0;
    int working = 1; // True while working
    while (working) {

        int lineIndex = 0;
        char character;
        while (character != '\n') {
            scanf("%s", &character);
            printf("%c", character);
        }




        printf("%s", line);

        int argumentState = 0;
        int argCharIndex = 0;
        int numSpaces = 0;

        char arg1[BUFFER_SIZE];
        char arg2[BUFFER_SIZE];
        char arg3[BUFFER_SIZE];
        for (int c = 0; c < strlen(line); c++) {
            switch (argumentState) {
                case 0: // Argument 1
                    if (line[c] == ' ') {
                        argumentState = 1;
                        argCharIndex = 0;
                        numSpaces++;
                    }
                    else {
                        arg1[argCharIndex] = line[c];
                    }
                    break;
                case 1: // Argument 2
                    if (line[c] == ' ') {
                        argumentState = 2;
                        argCharIndex = 0;
                        numSpaces++;
                    }
                    else {
                        arg2[argCharIndex] = line[c];
                    }
                    break;
                case 2: // Argument 3
                    if (line[c] == ' ') {
                        argumentState = 3;
                        numSpaces++;
                    }
                    else {
                        arg3[argCharIndex] = line[c];
                    }
                    break;
            }
        }
        
        if (numSpaces == 0) { // New case study
            char burdenStr[BUFFER_SIZE];
            itoa(burden, burdenStr, 10);
            // printf("%s\n",burdenStr);

            burden = 0;
        }
        else { // Add farmer to burden
            int args[3];
            args[0] = atoi(arg1);
            args[1] = atoi(arg2);
            args[2] = atoi(arg3);

            if (args[2] != 0) { // Check to make sure there are animals at the farm
                burden += args[0] * args[1];
            }
        }
    }

    // One more time at the end
    char burdenStr[BUFFER_SIZE];
    itoa(burden, burdenStr, 10);
    // printf("%s\n",burdenStr);
    
    return 0;
}