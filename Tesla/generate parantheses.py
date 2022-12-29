
def generateParenthesis(n):
    res = []

    def dfs(s=[], openN=0, closeN=0):
        if len(s) == 2*n:
            res.append("".join(s))
        if openN < n:
            s.append("(")
            dfs(s, openN+1, closeN)
            s.pop()
        if closeN < openN:
            s.append(")")
            dfs(s, openN, closeN+1)
            s.pop()
    dfs()
    return res

# Approach is opening paranthese is important first we should add ( then we can
# think about ).
# Time and space complexity is tricky to calculate.
