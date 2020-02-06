from typing import List


# sort str, time complexity O(NKlogK)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            ordered_s = sorted(s)
            ordered_s = ''.join(ordered_s)
            if ordered_s not in d:
                d[ordered_s] = [s, ]
            else:
                d[ordered_s].append(s)
        results = []
        for k in d:
            results.append(d[k])
        return results


# count numbers of character appearances, time complexity O(NK)
class SolutionV2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            count = tuple(count)
            if count not in d:
                d[count] = [s, ]
            else:
                d[count].append(s)
        results = []
        for k in d:
            results.append(d[k])
        return results
