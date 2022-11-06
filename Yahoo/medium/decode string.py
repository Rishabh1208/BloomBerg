#  s = "2[abc]3[cd]ef"
def decodeString(self, s):
    stack = []

    # iterate till you find first closing bracket "]" and then
    # until you find first opening bracket and then next top most
    # element in the stack would be a digit, multiply with it
    # and append in to the stack again.
    for i in range(len(s)):
        if s[i] != ']':
            stack.append(s[i])
        else:
            letter = ''
            while stack and stack[-1] != '[':
                letter = stack.pop() + letter
            stack.pop()

            # reason why we are taking digit as string is there might be chances that we might have 2 or 3 digit instead of 1.
            digit = ''
            while stack and stack[-1].isdigit():
                digit = stack.pop() + digit

            stack.append(int(digit) * letter)

    return "".join(stack)
