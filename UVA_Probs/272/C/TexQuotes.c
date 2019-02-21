#include <stdio.h>
#include <string.h>

int main() {
    char input;
    int counter = 0;
    while (scanf("%c", &input) == 1) {
        if (input == '"') {
            if (counter%2 == 0) {
                printf("%s", "``");
            }
            else {
                printf("%s", "''");
            }
            counter ++;
        }
        else {
            printf("%c", input);
        }
    }
    return 0;
}