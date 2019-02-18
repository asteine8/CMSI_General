#include <stdio.h>
#include <string.h>
#include <cstdlib>

#define BUFFER_SIZE 4096

#define true 1
#define false 0

void GetTextFromFile(char **buffer) {
    FILE *f = fopen("272.in", "r");
    char *text = (char *)malloc(BUFFER_SIZE);
    int i = 0;
    while (fgetc(f) != feof(f)) {
        text[i] = fgetc(f);
        i++;
    }
    fclose(f);
    *buffer = text;
}

int main() {
    
    char *inputString;
    GetTextFromFile(&inputString);
    char newText[BUFFER_SIZE<<2];

    printf("Input: %s", inputString);

    int iCount = 0;
    int isGrave = true;
    for (int i = 0; i < sizeof(inputString); i++) {
        if (inputString[i] == '"') {
            // quoteIndexs[iCount] = i;
            // iCount++;
            newText[iCount] = (isGrave) ? '`' : '\'';
            newText[iCount+1] = (isGrave) ? '`' : '\'';
            iCount += 2;
            isGrave = (isGrave) ? false : true;
        }
        else {
            newText[iCount] = inputString[i];
            iCount++;
        }
    }
    // printf("%s",fileBuffer);
    printf("%s",newText);
    
    return 0;
}