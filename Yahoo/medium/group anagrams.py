import collections


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)

    for s in strs:
        count = [0] * 26
        for ele in s:
            count[ord(ele) - ord('a')] += 1
        result[tuple(count)].append(s)
    return result.values()
