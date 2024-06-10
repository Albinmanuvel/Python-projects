def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Example usage
numbers = [5, 2, 8, 1, 9, 3]
target = 9
result = linear_search(numbers, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")
    