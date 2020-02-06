class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowles = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] in vowles:
                if s[right] in vowles:
                    t = s[left]
                    s[left] = s[right]
                    s[right] = t
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                if s[right] in vowles:
                    left += 1
                else:
                    left += 1
                    right -= 1
        s = ''.join(s)
        return s
