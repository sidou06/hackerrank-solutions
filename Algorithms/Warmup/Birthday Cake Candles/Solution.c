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

// Complete the birthdayCakeCandles function below.
int birthdayCakeCandles(int ar_count, int* ar) 
{
    int i , cpt = 1 , max = ar[0];  // Initialize counter and max to the first element
    for (i = 1; i < ar_count; i++)  // Loop through the array to find the max and count occurrences
    {
        if (ar[i] > max) { max = ar[i]; cpt = 1;}  // Update max and reset counter if a new max is found
        else if (ar[i] == max) cpt++;  // Increment counter if the current element equals the max
    }
    return cpt;  // Return the number of candles with the maximum height
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");  // Open the output file

    char* ar_count_endptr;
    char* ar_count_str = readline();  // Read the count of candles
    int ar_count = strtol(ar_count_str, &ar_count_endptr, 10);  // Convert the count to integer

    if (ar_count_endptr == ar_count_str || *ar_count_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate input

    char** ar_temp = split_string(readline());  // Read the array elements

    int* ar = malloc(ar_count * sizeof(int));  // Allocate memory for the array

    for (int i = 0; i < ar_count; i++) {  // Loop to read the integers into the array
        char* ar_item_endptr;
        char* ar_item_str = *(ar_temp + i);
        int ar_item = strtol(ar_item_str, &ar_item_endptr, 10);  // Convert string to integer

        if (ar_item_endptr == ar_item_str || *ar_item_endptr != '\0') { exit(EXIT_FAILURE); }  // Validate input

        *(ar + i) = ar_item;  // Store the item in the array
    }

    int result = birthdayCakeCandles(ar_count, ar);  // Call the function to get the result

    fprintf(fptr, "%d\n", result);  // Print the result to the output file

    fclose(fptr);  // Close the file

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