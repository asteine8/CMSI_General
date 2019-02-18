#include <stdio.h>

#define BUFFER_SIZE 100

int main() {

    char input[BUFFER_SIZE];

    printf("Enter a string: ");

    scanf("%s",&input);

    printf("You entered %s", input);
}