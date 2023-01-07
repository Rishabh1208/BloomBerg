

## APPROACH : CUSTOM SORTING WITH COMPARATOR ##
# MAIN IDEA : It's all about comparison . We define a func that compares two strings a ,b. \
# we consider a bigger than b if a+b > b+a . then we sort the numbers and concatenate them .
# a-> 3, b-> 30 => 330 > 303
## Things to note : Your comparator is supposed to return negative/zero/positive, 
# not a boolean. ##

# ALSO : We can use any type of sort, while sorting instead of comparing two numbers directly, 
# we can use the current comparator logic to compare and swap elements accordingly.

# Edge case : o/p -> "00" expected:"0"

## TIME COMPLEXITY : O(NlogN) ##
## SPACE COMPLEXITY : O(N) ##
def largestNumber(nums):
    import functools

    def comparator(s1, s2):
        if int(s1+s2) < int(s2+s1):
            return -1
        if int(s1+s2) > int(s2+s1):
            return 1
        return 0

    nums = [str(num) for num in nums]
    print("nums before", nums)
    
    nums = sorted(nums, key=functools.cmp_to_key(
        comparator),  reverse=True)
    # if the biggest number after sorting is 0 in first position, then rest all will
    # also be 0's so return 0

    print("nums", nums)
    ans = '0' if nums[0] == '0' else ''.join(nums)
    return ans


nums = [3, 30, 34, 5, 9]
print(largestNumber(nums))
