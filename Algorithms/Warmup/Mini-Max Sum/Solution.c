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

// Complete the miniMaxSum function below.
void miniMaxSum(int arr_count, int* arr) 
{
    long i , max = arr[0] , min = arr[0] , sum = arr[0] ;
    for (i=1 ; i<arr_count ; i++)  // Loop through the array to find the max, min, and sum
    {
        if (arr[i] > max) max = arr[i];  // Update max if the current element is greater
        if (arr[i] < min) min = arr[i];  // Update min if the current element is smaller
        sum += arr[i];  // Add the current element to sum
    }
    printf ("%ld %ld" , sum - max , sum - min);  // Print the result (sum excluding max and min)
}

int main()
{
    char** arr_temp = split_string(readline());  // Read and split the input string

    int* arr = malloc(5 * sizeof(int));  // Allocate memory for 5 integers

    for (int i = 0; i < 5; i++) {  // Loop to convert the input to integers and store in the array
        char* arr_item_endptr;
        char* arr_item_str = *(arr_temp + i);
        int arr_item = strtol(arr_item_str, &arr_item_endptr, 10);  // Convert string to integer

        if (arr_item_endptr == arr_item_str || *arr_item_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate input

        *(arr + i) = arr_item;  // Store the converted integer in the array
    }

    int arr_count = 5;

    miniMaxSum(arr_count, arr);  // Call the miniMaxSum function to compute and print the result

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

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");  // Tokenize the input string based on spaces

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);  // Allocate memory for the split tokens
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;  // Store the token in the splits array

        token = strtok(NULL, " ");  // Get the next token
    }

    return splits;
}