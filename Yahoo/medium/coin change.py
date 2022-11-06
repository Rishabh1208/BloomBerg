def coinChange(self, coins, amount):
    memo = [[-1 for i in range(amount+1)] for j in range(len(coins))]

    def dfs(i, amount):

        if i == 0:
            if amount % coins[0] == 0:
                return amount // coins[0]
            return float('inf')

        if memo[i][amount] != -1:
            return memo[i][amount]

        notPick = dfs(i-1, amount)
        pick = float('inf')
        if coins[i] <= amount:
            pick = 1 + dfs(i, amount - coins[i])

        memo[i][amount] = min(notPick, pick)
        return memo[i][amount]

    output = dfs(len(coins)-1, amount)
    return -1 if output == float('inf') else output
