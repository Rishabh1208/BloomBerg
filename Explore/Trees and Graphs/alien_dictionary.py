# words = ["wrt","wrf","er","ett","rftt"]
def alienOrder(words):
    adj = {}
    for word in words:
        for char in word:
            adj[char] = set()

    print("adj Before", adj)

    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        minLen = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:  # apex and ape
            return ""
        for i in range(minLen):
            if w1[i] != w2[i]:
                adj[w1[i]].add(w2[i])
                break
    print("adj after", adj)

    result = []
    visited, cycle = set(), set()

    def dfs(char):
        if char in cycle:
            return False
        if char in visited:
            return True

        cycle.add(char)
        for j in adj[char]:
            if not dfs(j):
                return False

        visited.add(char)
        cycle.remove(char)
        result.append(char)
        return True

    for char in adj:
        if not dfs(char):
            return ""

    return "".join(result[::-1])


words = ["wrt", "wrf", "er", "ett", "rftt"]
# words = ["a", "b", "c", "a"]
print(alienOrder(words))
