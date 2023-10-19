def find_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Get input from the user
try:
    num = int(input("Enter a number: "))
    factors_of_num = find_factors(num)
    print(f"Factors of {num} are: {', '.join(map(str, factors_of_num))}")

except ValueError:
    print("Please enter a valid integer.")

