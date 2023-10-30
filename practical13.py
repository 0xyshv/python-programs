def generate_fibonacci(n):
    """Returns the Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms for Fibonacci series: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_series = generate_fibonacci(n)
    print(f"Fibonacci series up to {n} terms: {', '.join(map(str, fibonacci_series))}")

#using recursion
# def fibonacci(n):
#     """Returns the nth term in the Fibonacci series."""
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input("Enter the number of terms for Fibonacci series: "))
# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     fibonacci_series = [fibonacci(i) for i in range(n)]
#     print(f"Fibonacci series up to {n} terms: {', '.join(map(str, fibonacci_series))}")

