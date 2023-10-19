def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get input from the user
try:
    num = int(input("Enter a number: "))
    print(f"{num} is {is_even_or_odd(num)}")
except ValueError:
    print("Please enter a valid integer.")

