# https://leetcode.com/discuss/interview-question/682583/Bloomberg-or-Phone-or-Order-list-in-welsh-alphabetical-order


alphabets = ['a', 'b', 'c', 'ch', 'dd', 'd', 'e', 'f', 'ff', 'g', 'ng', 'h', 'i',
             'j', 'l', 'll', 'm', 'n', 'o', 'p', 'ph', 'r', 'rh', 's', 't', 'th', 'u', 'w', 'y']
alpha_index = {}
for idx, val in enumerate(alphabets):
    alpha_index[val] = idx


def encode(s):
    ret = []
    i = 0
    while i < len(s)-1:
        if s[i] + s[i+1] in alpha_index:
            ret.append(alpha_index[s[i] + s[i+1]])
            i += 2
        else:
            ret.append(alpha_index[s[i]])
            i += 1
    if(i < len(s)):
        ret.append(alpha_index[s[len(s)-1]])
    return tuple(ret)


strings = ['abcd', 'abcdd', 'abcch']

arr = [(encode(x), x) for x in strings]
print("arr", arr)
arr.sort(key=lambda x: x[0])
print("afterSortarray", arr)
print([x for _, x in arr])
