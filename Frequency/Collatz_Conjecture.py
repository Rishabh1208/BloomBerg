# The Collatz Conjecture says if you take a positive integer N and repeatedly set either N=N/2 (if it's even) or N=3N+1 (if it's odd),
# N will eventually be 1.
# 5 -> 16 -> 8 -> 4 -> 2 -> 1 (5 steps).
# Given N, how many steps does it take to reach 1?

# const collatz = (num) => {
#     var steps = 0;
#     while (num !== 1 && num > 0) {
#         if (num % 2 === 0) {
#             num = num/2;
#             steps++;
#         } else if (num%2 !== 0){
#             num = 3*num +1;
#             steps++;
#         }
#     }
#     return steps;
# }

# Basic recursion approach

def collatz(num):

    def dfs(num):
        if num == 1:
            return 0

        if num % 2 == 0:
            steps = 1 + dfs(num//2)

        else:
            steps = 1 + dfs(num*3 + 1)

        return steps
    return dfs(num)

# Recursive solution with memoization

def collatz(num):
    memo = {1: 0}

    def dfs(num, memo):
        if memo[num]:
            return memo[num]

        if num % 2 == 0:
            steps = 1 + dfs(num//2)

        else:
            steps = 1 + dfs(num*3 + 1)

        memo[num] = steps
        return steps
    return dfs(num, memo)


def collatz(num, memo={1: 0}):
    if num in memo:
        return memo[num]

    if num % 2:
        res = 1 + collatz(3*num + 1, memo)
    else:
        res = 1 + collatz(num//2, memo)

    memo[num] = res
    return res

# Basic recursion approach
# private static int transformNum2(int num) {
# 	if(num == 1)
# 		return 0;
# 	return 1 + ( num % 2 == 0 ? transformNum2(num/2) : transformNum2(num*3 + 1));
# }
