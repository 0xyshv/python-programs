def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(char for char in s if char.isalnum()).lower()
    return clean_s == clean_s[::-1]

# Example usage:
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
