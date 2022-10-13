# The length of s is only up to 16, so it won't hurt if we exhaustively try out all possibility
# And intuitively backtracking + DFS is very good at doing job like this
# Check comment for more detail, pretty standard backtracking problem

# Time complexity: There are a total number of N characters in the string, so the number of gaps in between characters is N - 1. At each gap,
# we have 2 choices: whether or not to split at current position. In total we have O(2^N) possibilities.

# space complexity: o(n)
def maxUniqueSplit(s):
    res = [0]
    n = len(s)

    def dfs(i, count, visited):
        if i == n:
            res[0] = max(res[0], count)
            # stop condition
            return
        for j in range(i+1, n+1):
            # avoid re-visit/duplicates
            if s[i:j] in visited:
                continue
            # update visited set
            visited.add(s[i:j])
            # backtracking
            dfs(j, count+1, visited)
            # recover visited set for next possibility
            visited.remove(s[i:j])
    dfs(0, 0, set())  # function call
    return res[0]


s = "wwwzfvedwfvhsww"
print(maxUniqueSplit(s))
