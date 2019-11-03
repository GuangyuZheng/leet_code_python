class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) == 0:
            return []
        index1 = 0
        index2 = len(numbers) - 1

        tmp = numbers[index1] + numbers[index2]
        while tmp != target and index1 < index2:
            if tmp > target:
                index2 -= 1
            if tmp < target:
                index1 += 1
            tmp = numbers[index1] + numbers[index2]
        if tmp == target:
            return [index1 + 1, index2 + 1]
        else:
            return []
