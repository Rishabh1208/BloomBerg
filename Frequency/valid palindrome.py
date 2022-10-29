# Follow up: How would you make the string valid, if not valid ?
# https://leetcode.com/problems/valid-palindrome/

def isPalindrome(self, s):
    left = 0
    right = len(s)-1
    while(left < right):
        if left < right and not s[left].isalnum():
            left += 1
        elif left < right and not s[right].isalnum():
            right -= 1
        elif s[left].lower() == s[right].lower():
            left += 1
            right -= 1
        else:
            return False

    return True
