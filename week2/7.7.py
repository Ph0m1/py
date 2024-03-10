def is_palindrome(s):
    clean_s = ''.join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]
input_str = input()
if is_palindrome(input_str):
    print("yes")
else:
    print("no")