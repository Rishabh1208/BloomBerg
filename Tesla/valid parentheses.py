def isValid(self, s):

    preMap = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ele in s:
        if ele in preMap:
            if stack:
                s = stack.pop()
            else:
                s = "#"
            if s != preMap[ele]:
                return False

        else:
            stack.append(ele)

    return len(stack) == 0
