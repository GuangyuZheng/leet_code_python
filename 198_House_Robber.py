class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        profit = []
        for i in range(len(nums)):
            if i == 0:
                profit.append(nums[i])
            elif i == 1:
                profit.append(max(nums[i], nums[i - 1]))
            else:
                profit.append(max(profit[i - 1], profit[i - 2] + nums[i]))
        return profit[-1]
