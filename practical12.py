def factorial(n):
    """Returns the factorial of n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#using recursion
# def factorial(n):
#     """Returns the factorial of n."""
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
