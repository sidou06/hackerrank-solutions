#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();

// Complete the staircase function below.
void staircase(int n) 
{
    int i , j ;
    for (j=1 ; j<n+1 ; j++)  // Outer loop to handle each row
    {
        for (i=1 ; i<n-j+1 ; i++ ) printf(" ");  // Print spaces before the hashes
        for (i=n-j+1 ; i<n+1 ; i++ ) printf("#");  // Print hashes after the spaces
        printf ("\n");  // Move to the next line
    }
}

int main()
{
    char* n_endptr;
    char* n_str = readline();  // Read input for the number of steps
    int n = strtol(n_str, &n_endptr, 10);  // Convert the input to an integer

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate input

    staircase(n);  // Call the staircase function to print the pattern

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);  // Allocate memory for input

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);  // Read a line of input

        if (!line) { break; }

        data_length += strlen(cursor);  // Update the data length

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }  // Exit loop if newline is encountered

        size_t new_length = alloc_length << 1;  // Double the memory size if needed
        data = realloc(data, new_length);

        if (!data) { break; }  // If reallocation fails, exit

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';  // Remove newline character at the end
    }

    data = realloc(data, data_length);  // Resize to the actual data length

    return data;
}