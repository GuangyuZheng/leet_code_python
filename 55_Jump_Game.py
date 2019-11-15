from typing import List


# Simple backtracking, TLE
class SolutionTLE:
    def canJumpRecursive(self, start_position, nums: List[int]) -> bool:
        if start_position + nums[start_position] >= len(nums):
            return True
        for i in range(1, nums[start_position] + 1):
            if self.canJumpRecursive(start_position + i, nums) is True:
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1:
            return True
        return self.canJumpRecursive(0, nums)


# Top Down DP, still need backtracking, TLE
class SolutionTopDownDPTLE:
    def __init__(self, ):
        self.status = []

    def canJumpRecursive(self, start_position, nums: List[int]) -> bool:
        if self.status[start_position] == 1:
            return True
        elif self.status[start_position] == -1:
            return False
        else:
            if start_position + nums[start_position] >= len(nums):
                self.status[start_position] = 1
                return True
            for i in range(1, nums[start_position] + 1):
                if self.canJumpRecursive(start_position + i, nums) is True:
                    self.status[start_position] = 1
                    return True
            self.status[start_position] = -1
            return False

    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1:
            return True
        self.status = [0 for i in range(len(nums))]  # 0 unknown 1 good -1 bad
        self.status[-1] = 1
        result = self.canJumpRecursive(0, nums)
        return result


# Bottom Up DP, don't need backtracking, TLE
class SolutionBottomUpDPTLE:
    def __init__(self, ):
        self.status = []

    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1:
            return True
        self.status = [0 for i in range(len(nums))]  # 0 unknown 1 good -1 bad
        self.status[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            tmp = -1
            for j in range(1, nums[i] + 1):
                if self.status[min(i + j, len(nums) - 1)] == 1:
                    tmp = 1
                    break
            self.status[i] = tmp
        result = True if self.status[0] == 1 else False
        return result


class Solution:
    """
    Greedy Version, bottom up, find the leftmost position that can jump to the end (i.e leftmost_good)
    If the current position can reach the leftmost_good, then it becomes the new leftmost_good
    The result becomes whether 0 is the leftmost_good.
    In this way we can skip the search for right nums[i] statuses.
    """
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l <= 1:
            return True
        leftmost_good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= leftmost_good:
                leftmost_good = i
        result = leftmost_good == 0
        return result
