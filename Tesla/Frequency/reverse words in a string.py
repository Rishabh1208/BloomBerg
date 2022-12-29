from collections import deque


def reverseWords(s):
    # return " ".join(reversed(s.split()))
    low = 0
    high = len(s)-1
    while low < high and s[low] == " ":
        low += 1
        
    while low < high and s[high] == " ":
        high -= 1
        
    d, words = deque(), []
    while low <= high:
        if s[low] == " " and words:
            d.appendleft("".join(words))
            words = []
        elif s[low] != " ":
            words.append(s[low])
        low += 1
    d.appendleft("".join(words))
    return " ".join(d)
