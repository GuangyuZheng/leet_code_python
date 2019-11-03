class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n > 0:
            d = n % 26
            if d == 0:
                ch = 'Z'
                n = n - 1
            else:
                ch = chr(ord('A') + d - 1)
            result = ch + result
            n = n // 26
        return result
