class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [1 for i in range(0, n)]
        if n > 2:
            isPrime[2] = 1
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i] == 1:
                j = i * i
                while j < n:
                    isPrime[j] = 0
                    j += i
        cnt = 0
        for i in range(2, n):
            cnt += isPrime[i]
        return cnt
