from collections import deque


def killProcess(pid, ppid, kill):
    parent = {}

    for c, p in zip(pid, ppid):
        if p in parent:
            parent[p].append(c)
        else:
            parent[p] = [c]

    res = []
    q = deque([kill])

    while q:
        for _ in range(len(q)):
            k = q.popleft()
            res.append(k)

            if k in parent:
                q.extend(parent[k])

    return res
