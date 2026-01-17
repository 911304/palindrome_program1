from palindrome import check_palindrome

def test_palindrome_case1():
    assert check_palindrome("madam") is True

def test_palindrome_case2():
    assert check_palindrome("nurses run") is True

def test_palindrome_case3():
    assert check_palindrome("hello") is False

