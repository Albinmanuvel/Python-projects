def ternary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if lst[mid1] == target:
            return mid1
        elif lst[mid2] == target:
            return mid2
        elif target < lst[mid1]:
            right = mid1 - 1
        elif target > lst[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1

# Example usage
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
result = ternary_search(sorted_list, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")