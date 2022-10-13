# https://leetcode.com/discuss/interview-question/1603832/Bloomberg-or-Phone-Interview-New-Grad-or-Website-Browser-(LRU-Cache)


# Received the exact same question as this: 
# https://leetcode.com/discuss/interview-question/1575524/Bloomberg-Frankfurt-Office-or-Software-Engineer-Role-(New-Grad)-or-Phone-Interview-(Reject)

# Interviewer first asked what data structure design I would use to solve. 
# I recommended on a Map with a DLL and used illustration of inserting a URL 
# into the node, and checking to see if one exists, BEFORE I began to code.
# By illustrating removing a node/moving a node to the head, I was able to 
# prove to interviewer I understood the question + we were on the same page. 
# Then I began to code. I was asked some follow ups such as "What if you had a 
# capacity, how would you approach?" -> Basically LRU cache

# If there are no URL's (i.e. dummyHead is pointing to dummyTail) is there any reason 
# to do an if check so we just return an empty list?" -> yes I would still do an if 
# check to throw an exception
