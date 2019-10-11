class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            result = 0
            prev_one_step = 2
            prev_two_step = 1
            for i in range(3, n + 1):
                result = prev_one_step + prev_two_step
                prev_two_step = prev_one_step
                prev_one_step = result
            return result

