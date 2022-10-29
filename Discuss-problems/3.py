# First Problem: A process tree has crashed and you are given a sequence of it's nodes in random order,
# each representing a process and possible child(s). Each node has at most two child process.
# Find the root process node

# Input:
# {5 : [], 1: [2, 3], 4 : [], 3: [6], 6 : [], 2 : [4, 5]}

#  			1
#  		/      \
#  	2            3
#  /     \          /
#  4     5         6

# Output: 1

# https://leetcode.com/discuss/interview-question/1629220/Bloomberg-Phone-Interview ( same question )

def findProcessNodeBloomBerg(nodes):
    indegree = [0] * len(nodes)
    for key, value in nodes.items():
        for val in value:
            indegree[val-1] += 1
    for idx, val in enumerate(indegree):
        if val == 0:
            return idx + 1


nodes = {5: [], 1: [2, 3], 4: [], 3: [6], 6: [], 2: [4, 5]}
print(findProcessNodeBloomBerg(nodes))


def find_root_process(processes) -> int:
    if not processes:
        return -1

    mapping = {}

    for process in processes:
        id = process["id"]
        children = process["children"]

        if id not in mapping:
            mapping[id] = 0

        for child in children:
            mapping[child] = mapping.get(child, 0) + 1
    print("mapping", mapping)

    for key, value in mapping.items():
        if value == 0:
            return key

    return -1


processes = [
    {"id": 0, "children": [1, 2]},
    {"id": 1, "children": []},
    {"id": 2, "children": []},
]
print(find_root_process(processes))
