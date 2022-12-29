
def sumZero(n):
    maxLength = n//2
    remainder = n % 2
    arr = []
    if remainder != 0:
        arr.append(0)
    for i in range(1, maxLength+1):
        arr.append(i)
        arr.append(-i)
    return arr
