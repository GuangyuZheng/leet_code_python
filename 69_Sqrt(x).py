class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        mid = -1
        while start <= end:
            mid = (start + end) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 > x:
                end = mid - 1
            else:
                start = mid + 1
        if mid ** 2 > x:
            return mid - 1
        else:
            return mid
