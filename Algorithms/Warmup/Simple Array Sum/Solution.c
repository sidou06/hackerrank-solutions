#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to read a line from input
char* readline();

// Function to split a string into an array of strings
char** split_string(char*);

/*
 * Function to compute the sum of an array
 */
int simpleArraySum(int ar_count, int* ar) {
    int i, j = 0;
    for (i = 0; i < ar_count; i++) {
        j = j + ar[i];
    }
    return j;
}

int main() {
    // Open output file
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    // Read number of elements in array
    char* ar_count_endptr;
    char* ar_count_str = readline();
    int ar_count = strtol(ar_count_str, &ar_count_endptr, 10);

    // Validate input
    if (ar_count_endptr == ar_count_str || *ar_count_endptr != '\0') { 
        exit(EXIT_FAILURE); 
    }

    // Read array elements
    char** ar_temp = split_string(readline());
    int ar[ar_count];

    // Convert string array to integer array
    for (int ar_itr = 0; ar_itr < ar_count; ar_itr++) {
        char* ar_item_endptr;
        char* ar_item_str = ar_temp[ar_itr];
        int ar_item = strtol(ar_item_str, &ar_item_endptr, 10);

        // Validate input
        if (ar_item_endptr == ar_item_str || *ar_item_endptr != '\0') { 
            exit(EXIT_FAILURE); 
        }

        ar[ar_itr] = ar_item;
    }

    // Compute the sum of the array
    int result = simpleArraySum(ar_count, ar);

    // Print result to output file
    fprintf(fptr, "%d\n", result);

    // Close file
    fclose(fptr);

    return 0;
}

// Function to read a line from input
char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { 
            break; 
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { 
            break; 
        }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { 
            break; 
        }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

// Function to split a string into an array of strings
char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;
        token = strtok(NULL, " ");
    }

    return splits;
}