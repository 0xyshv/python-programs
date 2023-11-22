def calculate_series_sum(n):
    if n < 0:
        return "Invalid input. Please provide a non-negative integer."

    sum_value = 0
    factorial = 1

    for i in range(n + 1):
        if i != 0:
            factorial *= i
            sum_value += 1 / factorial

    return sum_value

# Example usage:
n = 5
result = calculate_series_sum(n)
print(f"The sum of the series for n={n} is: {result}")
