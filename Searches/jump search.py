import math

def jump_search(lst, target):
    n = len(lst)
    step = int(math.sqrt(n))
    prev = 0

    while lst[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    while lst[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if lst[prev] == target:
        return prev

    return -1

# Example :
sorted_list = input("Enter a sorted list of numbers separated by spaces: ").split()
sorted_list = [int(num) for num in sorted_list]
target = int(input("Enter the target number to search: "))

result = jump_search(sorted_list, target)

if result != -1:
    print(f"Target element {target} found at index {result}")
else:
    print(f"Target element {target} not found in the list")