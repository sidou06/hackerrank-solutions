#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

// Function to add two numbers
int solveMeFirst(int a, int b) {
    return a + b;
}

int main() {
    int num1, num2;
    // Read two integers from input
    scanf("%d %d", &num1, &num2);
    int sum;
    // Call function to calculate sum
    sum = solveMeFirst(num1, num2);
    // Print the sum
    printf("%d", sum);
    return 0;
}