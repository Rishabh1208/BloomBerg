def change(self, amount, coins):
    memo = [[-1 for i in range(amount+1)] for j in range(len(coins))]

    def dfs(i, amount):

        if i == 0:
            if amount % coins[0] == 0:
                return 1
            return 0

        if memo[i][amount] != -1:
            return memo[i][amount]

        notPick = dfs(i-1, amount)
        pick = 0
        if amount >= coins[i]:
            pick = dfs(i, amount-coins[i])

        memo[i][amount] = pick + notPick
        return memo[i][amount]

    return dfs(len(coins)-1, amount)
