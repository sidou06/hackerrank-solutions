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
char** split_string(char*);

// Complete the aVeryBigSum function below.
long long int aVeryBigSum(int ar_count, long* ar) 
{
    long long int i = 0;  // Initialize the sum to 0
    for (int j = 0; j < ar_count; j++)  // Loop through the array elements
    {
        i = i + ar[j];  // Add each element to the sum
    }
    return i;  // Return the total sum
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");  // Open file for output

    char* ar_count_endptr;
    char* ar_count_str = readline();  // Read the count of elements
    int ar_count = strtol(ar_count_str, &ar_count_endptr, 10);  // Convert to integer

    if (ar_count_endptr == ar_count_str || *ar_count_endptr != '\0') { exit(EXIT_FAILURE); }  // Exit if invalid input

    char** ar_temp = split_string(readline());  // Read the array elements

    long* ar = malloc(ar_count * sizeof(long));  // Allocate memory for the array

    for (int i = 0; i < ar_count; i++) {  // Loop through the array elements
        char* ar_item_endptr;
        char* ar_item_str = *(ar_temp + i);
        long ar_item = strtol(ar_item_str, &ar_item_endptr, 10);  // Convert each element to long

        if (ar_item_endptr == ar_item_str || *ar_item_endptr != '\0') { exit(EXIT_FAILURE); }  // Exit if invalid input

        *(ar + i) = ar_item;  // Assign the value to the array
    }

    long result = aVeryBigSum(ar_count, ar);  // Call the function to get the sum

    fprintf(fptr, "%ld\n", result);  // Write the result to the output file

    fclose(fptr);  // Close the file

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);  // Allocate memory for the input

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);  // Read a line of input

        if (!line) { break; }

        data_length += strlen(cursor);  // Update the data length

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }  // Break if the end of line is reached

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);  // Reallocate memory if needed

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';  // Remove newline character
    }

    data = realloc(data, data_length);  // Resize the memory to the exact length

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");  // Split the string by space

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);  // Reallocate memory for each token
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;  // Store the token

        token = strtok(NULL, " ");  // Get the next token
    }

    return splits;
}