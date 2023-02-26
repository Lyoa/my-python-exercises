# def isPalindrome(s):
#     if len(s) <= 1:
#         return True
#     else:
#         return (s[0] == s[-1]) and isPalindrome(s[1:-1])

# def display(s):
#     if isPalindrome(s):
#         print('That was a palindrome')
#     else:
#         print('That is not a palindrome')
# def isPalindrome(s):
#     if len(s) <= 1:
#       return s == s[::-1]
#     else:
#         return (s[0] == s[-1]) and isPalindrome(s[1:-1])

# def display(s):
#     if isPalindrome(s):
#         print('That was a palindrome')
#     else:
#         print('That is not a palindrome')

def isPalindrome(s):
      return s == s[::-1]

def display(s):
    if isPalindrome(s):
        return 'That was a palindrome'
    else:
        return 'That is not a palindrome'

display('racecar')
display('dad')

