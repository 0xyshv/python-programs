def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1

def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
target = int(input("Enter the number to search: "))

index = linear_search(lst, target)
if index != -1:
    print(f"Linear Search: {target} found at index {index}")
else:
    print(f"Linear Search: {target} not found in the list")

# Ensure the list is sorted for binary search
lst.sort()
index = binary_search(lst, target)
if index != -1:
    print(f"Binary Search: {target} found at index {index}")
else:
    print(f"Binary Search: {target} not found in the list")
