# s = "()[]{}"
def isValid(s):
    stack = []
    hashMap = {")": "(", "]": "[", "}": "{"}

    for ele in s:
        # closing
        if ele in hashMap:
            if stack:
                s = stack.pop()
            else:
                s = "#"
            if s != hashMap[ele]:
                return False

        else:
            stack.append(ele)
    return True
