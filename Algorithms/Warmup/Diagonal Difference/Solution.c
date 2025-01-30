#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char* ltrim(char*);
char* rtrim(char*);
char** split_string(char*);

int parse_int(char*);

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

int diagonalDifference(int arr_rows, int arr_columns, int** arr)
{
    int i,j=0,k=0;
    for(i=0 ; i<arr_rows ; i++)  // Loop through each row
    {
        j = j+arr[i][i];  // Sum the primary diagonal elements
        k = k+arr[i][arr_rows-i-1];  // Sum the secondary diagonal elements
    }
    return abs(k-j);  // Return the absolute difference between the diagonals
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");  // Open file for output

    int n = parse_int(ltrim(rtrim(readline())));  // Read the size of the matrix

    int** arr = malloc(n * sizeof(int*));  // Allocate memory for the 2D array

    for (int i = 0; i < n; i++) {
        *(arr + i) = malloc(n * (sizeof(int)));  // Allocate memory for each row of the matrix

        char** arr_item_temp = split_string(rtrim(readline()));  // Read the row elements

        for (int j = 0; j < n; j++) {
            int arr_item = parse_int(*(arr_item_temp + j));  // Convert each element to integer

            *(*(arr + i) + j) = arr_item;  // Store the element in the 2D array
        }
    }

    int result = diagonalDifference(n, n, arr);  // Call the function to get the diagonal difference

    fprintf(fptr, "%d\n", result);  // Write the result to the output file

    fclose(fptr);  // Close the file

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;

    char* data = malloc(alloc_length);  // Allocate memory for the input string

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);  // Read a line of input

        if (!line) {
            break;
        }

        data_length += strlen(cursor);  // Update the length of the input data

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;  // Exit when a newline character is encountered
        }

        alloc_length <<= 1;  // Double the allocated memory if needed

        data = realloc(data, alloc_length);  // Reallocate memory for the input data

        if (!data) {
            data = '\0';  // Set data to NULL if memory allocation fails
            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';  // Remove newline character at the end
    }

    data = realloc(data, data_length);  // Resize the memory to the exact length

    return data;
}

char* ltrim(char* str) {
    if (!str) {
        return '\0';  // Return NULL if the string is empty
    }

    if (!*str) {
        return str;  // Return the string if it is empty
    }

    while (*str != '\0' && isspace(*str)) {  // Skip leading whitespace
        str++;
    }

    return str;  // Return the string after trimming leading spaces
}

char* rtrim(char* str) {
    if (!str) {
        return '\0';  // Return NULL if the string is empty
    }

    if (!*str) {
        return str;  // Return the string if it is empty
    }

    char* end = str + strlen(str) - 1;

    while (end >= str && isspace(*end)) {  // Skip trailing whitespace
        end--;
    }

    *(end + 1) = '\0';  // Null-terminate the string after trimming spaces

    return str;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");  // Split the string by spaces

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);  // Reallocate memory for each token
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;  // Store the token

        token = strtok(NULL, " ");  // Get the next token
    }

    return splits;  // Return the array of tokens
}

int parse_int(char* str) {
    char* endptr;
    int value = strtol(str, &endptr, 10);  // Convert string to integer

    if (endptr == str || *endptr != '\0') {  // Exit if the conversion is invalid
        exit(EXIT_FAILURE);
    }

    return value;  // Return the converted integer
}