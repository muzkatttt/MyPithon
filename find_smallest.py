def find_smallest(arr):
    arr = [i for i in range(1, 11)]
    smallest = arr[0]
    smallest_index = [0]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index
    print(arr)

find_smallest(10)