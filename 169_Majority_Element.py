class Solution(object):

    # Hash map version
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] = d[num] + 1
        for k, v in d.items():
            if v > len(nums) // 2:
                return k

    # Boyer-Moore Majority Vote algorithm
    def majorityElementV2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                result = num
                cnt += 1
                continue
            if num != result:
                cnt -= 1
            else:
                cnt += 1
        return result
