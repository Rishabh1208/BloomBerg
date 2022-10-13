# At first, we talked for a few minutes about my background and interests then went on to discuss my
# projects.

# After that, they had me solve a program regarding trees. Have never really seen it before but the
# basic idea
# was you have an array of ids and a list of their corresponding children. It was in the context of
# operating
# system failures and the goal was to get the first failure (aka one of the array of ids).
# Went through the input given with the interviewer and realized that this was just looking for the
# root of the tree,
# being the first process failure. Had a bit of help but worked through a solution and coded it up.
# He said we don't
# usually have enough time to test with this but said code looks good to him.


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
