def interpolation_search(lst, target):
    low = 0
    high = len(lst) - 1

    while low <= high and target >= lst[low] and target <= lst[high]:
        pos = low + int(((float(high - low) / (lst[high] - lst[low])) * (target - lst[low])))

        if lst[pos] == target:
            return pos
        elif lst[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1

# Example :
sorted_list = input("Enter a sorted list of numbers separated by spaces: ").split()
sorted_list = [int(num) for num in sorted_list]
target = int(input("Enter the target number to search: "))

result = interpolation_search(sorted_list, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")