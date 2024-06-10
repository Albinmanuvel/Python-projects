def binary_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = binary_search(sorted_list, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")