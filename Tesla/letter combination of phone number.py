def letterCombinations(digits):
    letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    if len(digits) == 0:
        return []
    res = []

    def backtrack(index, path):
        if len(path) == len(digits):
            res.append("".join(path))
            return

        for ele in letters[digits[index]]:
            path.append(ele)
            backtrack(index+1, path)
            path.pop()

    backtrack(0, [])
    return res
