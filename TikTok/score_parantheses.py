# cur record the score at the current layer level.

# If we meet '(',
# we push the current score to stack,
# enter the next inner layer level,
# and reset cur = 0.

# If we meet ')',
# the cur score will be doubled and will be at least 1.
# We exit the current layer level,
# and set cur += stack.pop() + cur

def scoreOfParentheses(s):
    stack = []
    cur = 0
    for c in s:
        if c == '(':
            stack.append(cur)
            cur = 0
        else:
            if stack:
                cur = stack.pop() + max(1, cur*2)
    return cur

# S = "(((()()())))"
#   = "(((" 1 + 1 + 1 ")))"    // After replacing completed "()"s with 1s
#   = (1 + 1 + 1) * 2^3        // Applying the power operations
#   = 2^3 + 2^3 + 2^3          // Through the distributive property of multiplication

def scoreOfParentheses(S):
    pwr, ans = 0, 0
    for i in range(1, len(S)):
        if S[i] == "(":
            pwr += 1
        elif S[i-1] == "(":
            ans += 1 << pwr
            pwr -= 1
        else:
            pwr -= 1
    return ans


s = "))"
print(scoreOfParentheses(s))
