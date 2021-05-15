#include <stdio.h>
#include <stdlib.h>

int main() {

    char operator;
    double first, second;

    printf("Enter the first number: ");
    scanf("%lf", &first);

    printf("Enter the second number: ");
    scanf("%lf", &second);

    if (first + second == 1208 && first * second == 261775) {
        FILE * fptr;
        fptr = fopen("flag.txt", "r");
        printf ("ACCESS GRANTED. Here is the flag: ");
        char c = fgetc(fptr);
        while (c != EOF)
        {
            printf ("%c", c);
            c = fgetc(fptr);
        }

        fclose(fptr);
    } else {
        printf("Those weren't the right numbers, your friends have been compacted. Goodbye!\n");
        exit(0);
    }

    return 0;
}
