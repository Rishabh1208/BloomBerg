
from collections import defaultdict
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


class Leaderboard(object):

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId, score):
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K):
        heap = []
        for key, value in self.scores.items():
            heapq.heappush(heap, value)
            if len(heap) > K:
                heapq.heappop(heap)

        total = 0
        for ele in heap:
            total += ele
        return total

    def reset(self, playerId):
        self.scores[playerId] = 0


# ...............................................................................

# O(logN) for addScore. This is because each addition to the BST takes a logarithmic time for search.
# The addition itself once the location of the parent is known, takes constant time.

# O(logN) for reset since we need to search for the score in the BST and then update/remove it.
# Note that this complexity is in the case when every player always maintains a unique score.

# It takes O(K) for our top function since we simply iterate over the keys of the TreeMap and
# stop once we're done considering K scores.
# Note that if the data structure doesn't provide a natural
# iterator, then we can simply get a list of all the key-value pairs and they will naturally be sorted
# due to the nature of this data structure. In that case, the complexity would be O(N)O(N) since we
# would be forming a new list.

# SortedDict --> internally uses Balanced Binary search Tree which has add/remove/update in logn time.
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


# Quick Select Approach

class Leaderboard(object):

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId, score):
        if playerId not in self.scores:
            self.scores[playerId] = 0
        self.scores[playerId] += score

    def top(self, K):
        unsorted = list(self.scores.values())
        nums = self.findKthLargest(unsorted, K)
        return nums

    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]
        return fill

    def findKthLargest(self, nums, k):
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return sum(nums[k:])

    def reset(self, playerId):
        self.scores[playerId] = 0
