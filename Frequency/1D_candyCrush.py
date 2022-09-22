
# subtle difference between remove duplicates from array 2 and this.
def candy_crush(input):
    if not input:
        return input

    stack = []
    stack.append([input[0], 1])

    for i in range(1, len(input)):
        if stack[-1][0] != input[i]:
            if stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == input[i]:
                stack[-1][1] += 1
            else:
                stack.append([input[i], 1])
        else:
            stack[-1][1] += 1

    # handle end
    if stack[-1][1] >= 3:
        stack.pop()

    return "".join(c*cnt for c, cnt in stack)


print(candy_crush("aaaabbbc"))  # c
print(candy_crush("aabbbacd"))  # cd
print(candy_crush("aabbccddeeedcba"))  # blank expected
print(candy_crush("aabbbaacd"))  # cd
print(candy_crush("dddabbbbaccccaax"))  # x
