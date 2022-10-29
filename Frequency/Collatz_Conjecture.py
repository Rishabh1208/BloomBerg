# The Collatz Conjecture says if you take a positive integer N and repeatedly set either N=N/2
# (if it's even) or N=3N+1 (if it's odd),
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


def collatz(n):

    memo = {1: 0}

    def dfs(n):
        if n in memo:
            return memo[n]

        if n % 2 == 1:
            result = 1 + collatz(3*n+1)

        else:
            result = 1 + collatz(n//2)

        memo[n] = result
        return memo[n]
    return dfs(n)


# Basic recursion approach
# private static int transformNum2(int num) {
# 	if(num == 1)
# 		return 0;
# 	return 1 + ( num % 2 == 0 ? transformNum2(num/2) : transformNum2(num*3 + 1));
# }
