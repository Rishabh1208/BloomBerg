# https://leetcode.com/discuss/interview-question/1013880/Bloomberg-or-Phone-%2B-Onsite-or-Interview-Questions

# Phone Interview

# Given an array of securities and its associated price, return the top K stocks
# Similar to https://leetcode.com/problems/top-k-frequent-words/ and https://leetcode.com/problems/design-a-leaderboard

# Onsite Interview (2 rounds of technical, each round started with resume overview, why Bloomberg?)

# Round 1

# Word Search (https://leetcode.com/problems/word-search/)
# 1D Candy Crush (https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/)

# Round 2

# Number of ways to purchase oil (https://leetcode.com/discuss/interview-question/550259/bloomberg-phone-interview-se-grad-2020)
# This one was not listed, but brought up once on a post back in May 2020. Caught me off guard and wasn't able to solve it. Looking at discussion post, it seems to be a blend of https://leetcode.com/problems/subsets/ and dp(?)
# Valid BST (https://leetcode.com/problems/validate-binary-search-tree/)
# Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
# Follow up: How would you make the string valid, if not valid ?


def combinations(nums, target):

    def dfs(i, target):
        if target == 0:
            return 1

        if i == 0:
            if target % nums[i] == 0:
                return 1
            else:
                return 0

        notPick = dfs(i-1, target)
        pick = 0
        if nums[i] <= target:
            pick = dfs(i, target - nums[i])
        return notPick + pick

    return dfs(len(nums)-1, target)


nums = [10, 15, 50]
target = 60

print(combinations(nums, target))
