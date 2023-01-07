def multiply(num1, num2):
    if "0" in [num1, num2]:
        return "0"
    
    res = [0] * (len(num1)+len(num2))
    num1 = num1[::-1]
    num2 = num2[::-1]
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit = int(num1[i]) * int(num2[j])
            res[i+j] += digit
            res[i+j+1] += (res[i+j]//10)
            res[i+j] = res[i+j] % 10
    res = res[::-1]
    z = 0
    while z < len(res) and res[z] == 0:
        z += 1
    res = map(str, res[z:])
    return "".join(res)


num1 = "123"
num2 = "456"
