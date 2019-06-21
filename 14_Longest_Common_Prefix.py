from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        s = strs[0]
        prefix = ""
        for i in range(len(s)):
            for string in strs[1:]:
                if len(string) <= i:
                    return prefix
                if string[i] != s[i]:
                    return prefix
            prefix += s[i]
        return prefix
