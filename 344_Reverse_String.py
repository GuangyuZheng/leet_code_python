from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(int(l//2)):
            t = s[i]
            s[i] = s[l-1-i]
            s[l-1-i] = t

