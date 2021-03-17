def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False



print(is_palindrome('abccba'))
print(is_palindrome('aziza'))
print(is_palindrome('XYZwZYX'))
print(is_palindrome('abdcba'))
