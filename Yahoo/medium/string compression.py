def compress(chars):
    index = 0
    i = 0

    while i < len(chars):
        j = i

        while j < len(chars) and chars[j] == chars[i]:
            j += 1

        chars[index] = chars[i]
        index += 1
        if j - i > 1:
            for ele in str(j-i):
                chars[index] = ele
                index += 1

        i = j

    return index, chars[:index]


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress(chars))
