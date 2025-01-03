def is_palindrome(number):
    num_str = str(number)
    return num_str == num_str[::-1]

input_number = 12321
if is_palindrome(input_number):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")







