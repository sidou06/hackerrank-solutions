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

// Function to read a line from input
char* readline();

// Function to trim leading whitespace
char* ltrim(char*);

// Function to trim trailing whitespace
char* rtrim(char*);

// Function to split a string into an array of strings
char** split_string(char*);

// Function to compare two triplets and return scores
int* compareTriplets(int a_count, int* a, int b_count, int* b, int* result_count) {
    *result_count = 2;
    int *res = malloc(2 * sizeof(int));
    *res = 0;
    *(res + 1) = 0;
    for (int i = 0; i < 3; i++) {
        if (a[i] > b[i]) (*res)++;
        else if (a[i] < b[i]) (*(res + 1))++;
    }
    return res;
}

int main() {
    // Open output file
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    // Read first triplet
    char** a_temp = split_string(rtrim(readline()));
    int* a = malloc(3 * sizeof(int));

    for (int i = 0; i < 3; i++) {
        char* a_item_endptr;
        char* a_item_str = *(a_temp + i);
        int a_item = strtol(a_item_str, &a_item_endptr, 10);

        if (a_item_endptr == a_item_str || *a_item_endptr != '\0') { 
            exit(EXIT_FAILURE); 
        }

        *(a + i) = a_item;
    }

    int a_count = 3;

    // Read second triplet
    char** b_temp = split_string(rtrim(readline()));
    int* b = malloc(3 * sizeof(int));

    for (int i = 0; i < 3; i++) {
        char* b_item_endptr;
        char* b_item_str = *(b_temp + i);
        int b_item = strtol(b_item_str, &b_item_endptr, 10);

        if (b_item_endptr == b_item_str || *b_item_endptr != '\0') { 
            exit(EXIT_FAILURE); 
        }

        *(b + i) = b_item;
    }

    int b_count = 3;

    // Compute the result
    int result_count;
    int* result = compareTriplets(a_count, a, b_count, b, &result_count);

    // Print result
    for (int i = 0; i < result_count; i++) {
        fprintf(fptr, "%d", *(result + i));
        if (i != result_count - 1) {
            fprintf(fptr, " ");
        }
    }

    fprintf(fptr, "\n");

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

        alloc_length <<= 1;
        data = realloc(data, alloc_length);

        if (!data) {
            data = '\0';
            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
        data = realloc(data, data_length);

        if (!data) {
            data = '\0';
        }
    } else {
        data = realloc(data, data_length + 1);
        if (!data) {
            data = '\0';
        } else {
            data[data_length] = '\0';
        }
    }

    return data;
}

// Function to trim leading whitespace
char* ltrim(char* str) {
    if (!str) {
        return '\0';
    }
    if (!*str) {
        return str;
    }
    while (*str != '\0' && isspace(*str)) {
        str++;
    }
    return str;
}

// Function to trim trailing whitespace
char* rtrim(char* str) {
    if (!str) {
        return '\0';
    }
    if (!*str) {
        return str;
    }
    char* end = str + strlen(str) - 1;
    while (end >= str && isspace(*end)) {
        end--;
    }
    *(end + 1) = '\0';
    return str;
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