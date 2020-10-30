//This program will print the output Hello world on the console

#include <stdio.h>

// Variables

int varInteger = 100;
float varFloat = 1.103;
double varDouble = 20.20;
char varChar = 'C';
char varString[12] = "Hello world";

// Function creation type void
void printFunction(){
    printf("It works!\n");
}

// Function creation type int
int sumFunction(int firstValue, int secValue){
    int sumResult = firstValue + secValue;
    return sumResult;
}


int main(){
    // Testing different var types and print fuction
    printf("This is an Integer value... %d\n", varInteger);
    printf("This is a float value... %lf\n", varFloat);
    printf("This is a Double value... %lf\n", varDouble);
    printf("This is a Char value... %c\n", varChar);
    printf("This is a multiple Char value... %s\n", varString);

    // Testing function type void call
    printf("Testing void function call... ");
    printFunction();

    // Testing function type int call
    printf("Testing function value return... %d\n", sumFunction(2, 1));

    // End of execution
    return 0;
}

