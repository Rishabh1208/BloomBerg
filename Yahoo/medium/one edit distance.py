def isOneEditDistance(self, s, t):
    if abs(len(s) - len(t)) > 1 or s == t:
        return False

    found_inequality = False
    i = j = 0

    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            if found_inequality:
                return False
            found_inequality = True
            if len(s) < len(t):
                i -= 1
            elif len(s) > len(t):
                j -= 1
        i += 1
        j += 1

    return True
