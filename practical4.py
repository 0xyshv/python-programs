def print_factors(n):
    print(f"Factors of {n} are:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

# Get user input
user_input = int(input("Enter a number: "))

# Call the function to print factors
print_factors(user_input)


