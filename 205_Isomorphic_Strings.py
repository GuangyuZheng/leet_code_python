class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for i in range(len(s)):
            ch_s, ch_t = s[i], t[i]
            if ch_s not in d1:
                if ch_t not in d2:
                    d1[ch_s] = ch_t
                    d2[ch_t] = ch_s
                else:
                    return False
            else:
                if d1[ch_s] != ch_t or d2[ch_t] != ch_s:
                    return False
        return True
