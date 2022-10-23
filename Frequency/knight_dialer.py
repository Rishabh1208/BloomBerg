# Recursion with memoization
def knightDialer(n):
    neighbors = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [
        0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
    memo = {}

    def dfs(i, n):
        if n == 1:
            return 1

        if (i, n) in memo:
            return memo[(i, n)]

        count = 0
        for nei in neighbors[i]:
            count += dfs(nei, n-1)

        memo[(i, n)] = count
        return memo[(i, n)]

    result = 0
    for i in range(10):
        result += dfs(i, n)
    return result % (10 ** 9 + 7)

# DP
def knightDialer(N):
    # Neighbors maps K: starting_key -> V: list of possible destination_keys
    neighbors = {
        0: (4, 6),
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (0, 3, 9),
        5: (),
        6: (0, 1, 7),
        7: (2, 6),
        8: (1, 3),
        9: (2, 4)
    }
    current_counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(N-1):
        next_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print(current_counts)
        for src_key in range(10):
            for dst_key in neighbors[src_key]:
                next_counts[dst_key] = (
                    next_counts[dst_key] + current_counts[src_key]) % (10**9 + 7)
        current_counts = next_counts
    print("final", current_counts)
    return sum(current_counts) % (10**9 + 7)


n = 2
print(knightDialer(n))
