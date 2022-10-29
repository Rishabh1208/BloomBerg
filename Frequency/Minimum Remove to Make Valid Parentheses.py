def minRemoveToMakeValid(s):
    li = list(s)
    stack = []
    for i in range(len(li)):
        if li[i] == "(":
            stack.append(i)
        elif li[i] == ")":
            if stack:
                stack.pop()
            else:
                li[i] = ""
    while len(stack) != 0:
        li[stack.pop()] = ""
    return "".join(li)


def minRemoveToMakeValid(s):
    open = 0
    s = list(s)
    # Remove invalid ")"
    for i, c in enumerate(s):
        if c == '(':
            open += 1
        elif c == ')':
            if not open:
                s[i] = ""
            else:
                open -= 1

    # Remove the rightmost "("
    for i in range(len(s)-1, -1, -1):
        if not open:
            break
        if s[i] == '(':
            s[i] = ""
            open -= 1

    return "".join(s)
