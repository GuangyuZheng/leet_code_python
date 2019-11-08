class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []
        while True:
            n = sum(int(i)**2 for i in str(n))
            if n == 1:
                return True
            else:
                if n in visited:
                    return False
                else:
                    visited.append(n)
