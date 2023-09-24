def check_palindrome(input_str):
    input_str = str(input_str)
    input_str = input_str.replace(" ", "").lower()
    return input_str == input_str[::-1]

user_input = input("Enter a string or integer: ")
if check_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
