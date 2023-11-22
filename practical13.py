def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < n:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)

    return fibonacci_series

# Example usage:
num_terms = 10
fibonacci_result = generate_fibonacci(num_terms)
print(f"The Fibonacci series with {num_terms} terms is: {fibonacci_result}")
