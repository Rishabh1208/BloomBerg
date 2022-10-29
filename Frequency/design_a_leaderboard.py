
from sortedcontainers import SortedDict
import heapq

# O(1) for addScore.
# O(1) for reset.
# O(NlogN) for top where NN represents the total number of 
# players since we sort all of the player scores and then take the top K from the sorted list.

# O(1) for addScore.
# O(1) for reset.
# O(K)+O(NlogK) = O(NlogK). 
# It takes O(K) to construct the initial heap and then for the 
# rest of the N−K elements, we perform the extractMin and add operations on the heap each of 
# which take (logK) time.
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K: int) -> int:

        # This is a min-heap by default in Python.
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


# ...............................................................................

# O(logN) for addScore. This is because each addition to the BST takes a logarithmic time for search. 
# The addition itself once the location of the parent is known, takes constant time.
# O(logN)O(logN) for reset since we need to search for the score in the BST and then update/remove it. 
# Note that this complexity is in the case when every player always maintains a unique score.
# It takes O(K)O(K) for our top function since we simply iterate over the keys of the TreeMap and 
# stop once we're done considering K scores. Note that if the data structure doesn't provide a natural 
# iterator, then we can simply get a list of all the key-value pairs and they will naturally be sorted 
# due to the nature of this data structure. In that case, the complexity would be O(N)O(N) since we 
# would be forming a new list.
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with
        # key as the score and value as the number of players that have
        # that score.
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1

            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore,
                                                                 0) + 1

    def top(self, K: int) -> int:
        count, total = 0, 0

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times):
                total += -key
                count += 1

                # Found top-K scores, break.
                if count == K:
                    break

            # Found top-K scores, break.
            if count == K:
                break

        return total

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]
