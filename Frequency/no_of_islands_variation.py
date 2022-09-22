# At the beggining I was asked questions about my recent project and why I wanna join Bloomberg. I had one question:
# [[0,0,0,0,1,0,1,0],
# [0,0,1,1,1,1,1,0],
# [0,0,1,0,1,0,1,0],
# [0,0,1,1,1,1,1,0],
# [0,1,0,1,1,0,1,0]]
# You need to find a number of lakes, so 0 which are surrounded with 1, if it touches the border, than it is ocean water,
# it is similar to number of islands . The whole interview is around 45 - 60 min. You have last15 min to ask questions.


# Well so technically all the water which touches borders is ocean water. Then we have lands, where inside of them we have lakes.
# One land can have 1,2,... lakes.
# You need to find a number of lakes. So I used dfs from each border to turn all the ocean water to 2, then your problem becomes 
# https://leetcode.com/problems/number-of-islands/ =)

def capture(nums):

    rows = len(nums)
    cols = len(nums[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or nums[r][c] != 0:
            return
        nums[r][c] = 2
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if nums[r][c] == 0 and (r in [0, rows-1] or c in [0, cols-1]):
                dfs(r, c)


nums = [[0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0]]

# numsResult = [[2, 2, 2, 2, 1, 2, 1, 2],
    #           [2, 2, 1, 1, 1, 1, 1, 2],
    #           [2, 2, 1, 0, 1, 0, 1, 2],
    #           [2, 2, 1, 1, 1, 1, 1, 2],
    #           [2, 1, 2, 1, 1, 2, 1, 2]]

print(capture(nums))
