class Solution:
    # brute force
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0
        for i in range(h_len - n_len + 1):
            sub_str = haystack[i: i + n_len]
            if sub_str == needle:
                return i
        return -1

    # Sunday Version
    def strStr_2(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if n_len == 0:
            return 0
        i = 0
        while i < h_len - n_len + 1:
            flag = True
            for j in range(n_len):
                if haystack[i+j] != needle[j]:
                    flag = False
                    if i+n_len < h_len:
                        if haystack[i+n_len] not in needle:
                            i = i + n_len
                        else:
                            i = i + n_len - needle.rfind(haystack[i+n_len])
                    else:
                        i += 1
                    break
            if flag:
                return i
        return -1
