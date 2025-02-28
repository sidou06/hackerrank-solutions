#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();

/*
 * Complete the maximumDraws function below.
 * This function calculates the maximum number of draws needed 
 * to guarantee at least one matching pair of socks.
 */
int maximumDraws(int n) {
    return n+1; // The worst-case scenario requires drawing (n+1) socks.
}

int main()
{
    // Open the output file for writing
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    // Read the number of test cases
    char* t_endptr;
    char* t_str = readline();
    int t = strtol(t_str, &t_endptr, 10);

    // Validate input
    if (t_endptr == t_str || *t_endptr != '\0') { exit(EXIT_FAILURE); }

    for (int t_itr = 0; t_itr < t; t_itr++) {
        // Read the value of n (number of different pairs of socks)
        char* n_endptr;
        char* n_str = readline();
        int n = strtol(n_str, &n_endptr, 10);

        // Validate input
        if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

        // Compute the result
        int result = maximumDraws(n);

        // Write the result to the output file
        fprintf(fptr, "%d\n", result);
    }

    // Close the output file
    fclose(fptr);

    return 0;
}

/*
 * Function to read a line of input dynamically.
 */
char* readline() {
    size_t alloc_length = 1024; // Initial buffer size
    size_t data_length = 0; 
    char* data = malloc(alloc_length); // Allocate memory for input

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; } // Stop if no more input

        data_length += strlen(cursor);

        // Break if newline is encountered or buffer has space left
        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        // Double the buffer size if necessary
        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; } // Stop if memory allocation fails

        alloc_length = new_length;
    }

    // Replace newline character with null terminator
    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    // Reallocate to fit actual input size
    data = realloc(data, data_length);

    return data;
}