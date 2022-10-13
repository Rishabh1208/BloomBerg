# https://leetcode.com/discuss/interview-question/522824/Bloomberg-or-Phone-or-New-Grad-SWE-(London)-next-round


# Write a function which returns True if called more than 3 times in 3 seconds

# The question, as you can see, was very vague. But I kept asking good / bad questions which made me work out a preliminary solution. I used a list to keep track of all call times and at each call, traversed the list from the end to the start to find if there are 3 calls which are within three seconds.

# After this, I was prompted to come up with a more optimal soltution which I had been thinking of anyway since I knew my first solution was sub-optimal. The key idea is that at each point, you just need to keep track of the latest 3 calls. So I came up with this:

# import deque

# calls = deque()
# num_calls = 0

# def calledMoreThan3Times():
# 	curr_time = get_time() # in seconds
	
# 	if num_calls<3:
# 		calls.append(curr_time)
# 		num_calls+=1
		
# 	else:
# 		calls.append(curr_time)
# 		calls.popleft()
	
# 	if num_calls == 3 and calls[2] - calls[0] <= 3: #seconds
# 		return True
		
# 	return False
		
# My suggestion would be to just keep communicating well throughout writing your code. Even if you are wrong, the interviewer will understand your thought process and maybe even correct you. Dont be afraid to make mistakes.