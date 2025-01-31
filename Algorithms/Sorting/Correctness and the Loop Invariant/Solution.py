def insertion_sort(l):
    # Loop through each element starting from the second one
    for i in range(1, len(l)):
        j = i - 1
        key = l[i]

        # Shift elements of l[0..i-1] that are greater than key
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j -= 1
        
        # Place key at its correct position
        l[j + 1] = key

m = int(input().strip())
ar = list(map(int, input().strip().split()))

insertion_sort(ar)

# Print the sorted array
print(" ".join(map(str, ar)))