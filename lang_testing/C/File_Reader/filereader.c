#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 100

int main() {

    // Get the filename from the terminal
    char fileName[BUFFER_SIZE];
    printf("Enter your filename: ");
    if (0 == scanf("%s", &fileName)) {
        printf("Invalid input");
        return 0;
    }
    
    // Get the file
    FILE *file;
    file = fopen(fileName, "r");
    if (file == NULL) {
        printf("File does not exist");
        return 0;
    }

    // Get the first line of the file (Or until eof marker)
    char line[BUFFER_SIZE];
    fgets(line, BUFFER_SIZE, file);

    printf("First Line:\n%s", line);
    printf("\nAll Lines:\n");

    while (fgets(line, BUFFER_SIZE, file) != NULL) {
        printf("%s", line);
    }

    return 0;
}