class Solution:
    def reverseWords(self, s: str) -> str:
        word_lists = []

        tmp_word = ""
        for ch in s:
            if ch == " ":
                if tmp_word != "":
                    word_lists.append(tmp_word)
                    tmp_word = ""
            else:
                tmp_word += ch
        if tmp_word != "":
            word_lists.append(tmp_word)

        results = ""
        for i in range(len(word_lists) - 1, -1, -1):
            if i != 0:
                results += word_lists[i] + ' '
            else:
                results += word_lists[i]
        return results


# C-like O(1), first reverse total, next reverse word one by one, finally remove redundant spaces
class SolutionV2:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        s.reverse()

        start, end = -1, -1
        i = 0
        while i < len(s):
            if s[i] == ' ':
                while start < end:
                    tmp = s[start]
                    s[start] = s[end]
                    s[end] = tmp
                    start += 1
                    end -= 1
                start, end = -1, -1
            else:
                if start != -1:
                    end += 1
                else:
                    start, end = i, i
            i += 1

        if start != -1:
            while start < end:
                tmp = s[start]
                s[start] = s[end]
                s[end] = tmp
                start += 1
                end -= 1

        j = 0
        while j < len(s):
            if s[j] == ' ':
                k = j
                while k < len(s) and s[k] == ' ':
                    k += 1
                if k > j:
                    s = s[:j + 1] + s[k:]
                    j -= (k - j) - 1
            j += 1

        return ''.join(s)
