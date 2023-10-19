try:
    n = int(input("Enter a size: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        for i in range(1, n + 1):
            print('*' * i)

except ValueError:
    print("Please enter a valid positive integer.")
