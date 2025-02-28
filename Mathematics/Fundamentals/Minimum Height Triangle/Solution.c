#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

/*
 * Function to calculate the minimum integer height required 
 * for a triangle with a given base and area.
 */
int lowestTriangle(int base, int area){
    if (area * 2 % base == 0) 
        return area * 2 / base; // If the division is exact, return the quotient
    else 
        return area * 2 / base + 1; // Otherwise, round up to the next integer
}

int main() {
    int base; 
    int area; 

    // Read base and area from input
    scanf("%d %d", &base, &area);

    // Compute the minimum required height
    int height = lowestTriangle(base, area);

    // Print the computed height
    printf("%d\n", height);

    return 0;
}