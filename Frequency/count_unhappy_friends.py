

def unhappyFriends(n,preferences, pairs):
    # person: ste of people they prefer over their partner
    
    d = {}
    
    for x, y in pairs:
        d[x] = set(preferences[x][:preferences[x].index(y)])
        d[y] = set(preferences[y][:preferences[y].index(x)])
        
    result = 0
    for x in d:
        for y in d[x]:
            if x in d[y]:
                result+=1
                break
    return result