def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Take input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]

# Perform selection sort
sorted_list = selection_sort(input_list)

# Print the sorted list
print("Sorted list:", sorted_list)
