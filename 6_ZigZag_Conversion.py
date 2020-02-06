class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        converted = [[] for i in range(numRows)]
        pos = 0
        direction = 1
        for ch in s:
            converted[pos].append(ch)
            pos += direction
            if pos == numRows-1:
                direction = -1
            if pos == 0:
                direction = 1
        results = ""
        for c in converted:
            results += ''.join(c)
        return results
