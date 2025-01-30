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

// Complete the plusMinus function below.
void plusMinus(int arr_count, int* arr) 
{
    int i , pos=0 , neg=0 , nul=0 ;
    for (i=0 ; i<arr_count ; i++)  // Loop through the array
    {
        if (arr[i]>0) pos++;  // Count positive numbers
        else
        {
            if (arr[i]<0) neg++;  // Count negative numbers
            else nul++;  // Count zeros
        }
    }
    printf("%f \n" , ((double) pos)/((double) arr_count));  // Print the proportion of positive numbers
    printf("%f \n" , ((double) neg)/((double) arr_count));  // Print the proportion of negative numbers
    printf("%f \n" , ((double) nul)/((double) arr_count));  // Print the proportion of zeros
}

int main()
{
    char* n_endptr;
    char* n_str = readline();  // Read the size of the array
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate the input

    char** arr_temp = split_string(readline());  // Read the array elements

    int* arr = malloc(n * sizeof(int));  // Allocate memory for the array

    for (int i = 0; i < n; i++) {
        char* arr_item_endptr;
        char* arr_item_str = *(arr_temp + i);
        int arr_item = strtol(arr_item_str, &arr_item_endptr, 10);

        if (arr_item_endptr == arr_item_str || *arr_item_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate the input

        *(arr + i) = arr_item;  // Store the element in the array
    }

    int arr_count = n;

    plusMinus(arr_count, arr);  // Call the plusMinus function to calculate and print the proportions

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);  // Allocate memory for input string

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);  // Read a line of input

        if (!line) { break; }

        data_length += strlen(cursor);  // Update the length of the input data

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }  // Exit loop if newline character is encountered

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

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");  // Split the string by spaces

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);  // Reallocate memory for each token
        if (!splits) {
            return splits;  // Return if reallocation fails
        }

        splits[spaces - 1] = token;  // Store the token

        token = strtok(NULL, " ");  // Get the next token
    }

    return splits;  // Return the array of tokens
}