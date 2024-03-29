def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

# Example usage:
lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
sorted_list = insertion_sort(lst)
print(f"Sorted List: {sorted_list}")
