class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        m = 0
        for ch in s:
            if ch in sub_str:
                idx = sub_str.find(ch)
                m = max(m, len(sub_str))
                sub_str = sub_str[idx+1:]
                sub_str += ch
            else:
                sub_str += ch
        m = max(m, len(sub_str))
        return m
