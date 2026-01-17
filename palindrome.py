def ckeck_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if ckeck_palindrome(user_input):
        print(" It isPalindrome")
    else:
        print("It is Not Palindrome")