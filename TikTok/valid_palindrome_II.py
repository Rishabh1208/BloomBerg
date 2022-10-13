
# Brute force approach would be to delete a element one by one and compare by reversing it. 
# Time: O(n2)

# Better approach Two pointer approach, cuurently we are creating an extra space but that can be avoided by creating an helper function.
def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    # Time: O(n)
    # Space: O(n)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True
