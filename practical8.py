def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2

try:
    N = int(input("Enter a positive integer N: "))
    if N < 1:
        print("Please enter a positive integer.")
    else:
        total = sum_of_n_natural_numbers(N)
        print(f"The sum of the first {N} natural numbers is: {total}")

except ValueError:
    print("Please enter a valid positive integer.")
