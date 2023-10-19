def factorial(num):
    """Returns the factorial of a number."""
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def sum_series(n):
    """Calculates the sum of the series 1 + 1/1! + 1/2! + ... + 1/n!."""
    total = 0
    for i in range(n + 1):
        total += 1 / factorial(i)
    return total

# Example usage:
n = int(input("Enter a positive integer n: "))
result = sum_series(n)
print(f"The sum of the series up to {n} is: {result}")
