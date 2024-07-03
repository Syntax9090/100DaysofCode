def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
input_str = "Madam"
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")

