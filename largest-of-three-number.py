def find_largest(a, b, c):
    # Using the built-in max function
    return max(a, b, c)

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    largest = find_largest(num1, num2, num3)
    print(f"The largest number is: {largest}")

except ValueError:
    print("Please enter valid numbers.")

