class SolutionDP:
    def longestPalindrome(self, s: str) -> str:
        p = [[False for i in range(len(s))] for j in range(len(s))]
        max_len = -1
        p_str = ""
        for l in range(1, len(s)+1):
            for start in range(0, len(s)):
                end = start + l - 1
                if end >= len(s):
                    break
                else:
                    if start == end:
                        p[start][end] = True
                        if l > max_len:
                            max_len = l
                            p_str = s[start:end+1]
                    elif start + 1 == end:
                        if s[start] == s[end]:
                            p[start][end] = True
                            if l > max_len:
                                max_len = l
                                p_str = s[start:end+1]
                    else:
                        if s[start] == s[end] and p[start+1][end-1] is True:
                            p[start][end] = True
                            if l > max_len:
                                max_len = l
                                p_str = s[start:end+1]
        return p_str


class SolutionExpandFromMiddle:
    def expandFromMiddle(self, start, end, s: str) -> int:
        L, R = start, end
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L = L - 1
            R = R + 1
        return (R - 1) - (L + 1) + 1

    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        max_len = 1
        p_str = s[0]
        for i in range(len(s)):
            odd_len = self.expandFromMiddle(i, i, s)
            even_len = self.expandFromMiddle(i, i + 1, s)
            if odd_len > max_len:
                max_len = odd_len
                start = int(i - (odd_len - 1) / 2)
                end = int(i + (odd_len - 1) / 2)
                p_str = s[start:end + 1]
            if even_len > max_len:
                max_len = even_len
                start = int(i - (even_len - 2) / 2)
                end = int(i + 1 + (even_len - 2) / 2)
                p_str = s[start:end + 1]
        return p_str


