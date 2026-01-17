def check_palindrome(text):
    text = text.lower().replace(" ", "")
    result = (text == text[::-1])   
    return result                   


if __name__ == "__main__":
    text = input("Enter a string: ")
    print(check_palindrome(text))