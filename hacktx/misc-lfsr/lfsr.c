#include <stdio.h>
#include <stdlib.h>

int main(){

    int length = 5;

    printf("Please enter the bitstring you want to shift: ");
    char str[100];
    scanf("%s", str);

    char * end;
    unsigned int buffer = 0;
    unsigned int bufferMask = 0x1f;
    unsigned int leftMask = 0x08;
    unsigned int rightMask = 0x1;

    buffer = strtol(str, &end, 2);
    unsigned int input = buffer;

    printf("Please enter how many times you want to shift it: ");
    int rounds;
    scanf("%d", &rounds);

    for(int i = 0; i < rounds; i++){
        unsigned int new = ((buffer & leftMask) >> 3) ^ (buffer & rightMask);
        buffer = ((buffer << 1) & bufferMask) ^ new;
    }

    int inputBits[length];
    int bufferBits[length];

    int i = length;
    while(i){
        if(input & 0x1) inputBits[i-1] = 1;
        else inputBits[i-1] = 0;
        if(buffer & 0x1) bufferBits[i-1] = 1;
        else bufferBits[i-1] = 0;
        input = input >> 1;
        buffer = buffer >> 1;
        i--; 
    }

    printf("Input: ");
    for(int i = 0; i < length; i++){
        printf("%d", inputBits[i]);
    }

    printf("\nShift: %d", rounds);

    printf("\nOutput: ");
    for(int i = 0; i < length; i++){
        printf("%d", bufferBits[i]);
    }

    printf("\n");
}
