def isValid(self, s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ele in s:
        if ele in mapping:
            if stack:
                s1 = stack.pop()
            else:
                s1 = '#'
            if s1 != mapping[ele]:
                return False
        else:
            stack.append(ele)
    return not stack
