from typing import List


class Solution:
    def binarySearch(self, nums, begin, end, target):
        left = begin
        right = end
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

    def update_results(self, results, tmp_results):
        if -1 in tmp_results:
            return results
        else:
            concat = results + tmp_results
            return [min(concat), max(concat)]

    def searchRangeRecursive(self, nums, begin, end, target):
        results = []
        mid = (begin+end)//2
        if begin == end:
            if nums[mid] == target:
                return [mid, mid]
            else:
                return [-1, -1]
        left_p = self.binarySearch(nums, begin, mid, target)
        right_p = self.binarySearch(nums, mid+1, end, target)

        if left_p != -1:
            results.append(left_p)
        if right_p != -1:
            results.append(right_p)
        if len(results) == 0:
            results = [-1, -1]
        if len(results) == 1:
            results = results + results
        if left_p != -1:
            tmp_results = self.searchRangeRecursive(nums, begin, left_p-1, target)
            results = self.update_results(results, tmp_results)
            tmp_results = self.searchRangeRecursive(nums, left_p+1, mid, target)
            results = self.update_results(results, tmp_results)
        if right_p != -1:
            tmp_results = self.searchRangeRecursive(nums, right_p+1, end, target)
            results = self.update_results(results, tmp_results)
            tmp_results = self.searchRangeRecursive(nums, mid, right_p-1, target)
            results = self.update_results(results, tmp_results)
        return results

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.searchRangeRecursive(nums, 0, len(nums)-1, target)


class Solution2:
    def binarySearch(self, nums, target, search_left):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                if mid > 0 and nums[mid] == nums[mid-1] and search_left:
                    right = mid-1
                elif mid < len(nums)-1 and nums[mid] == nums[mid+1] and (not search_left):
                    left = mid+1
                else:
                    return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        results = [-1, -1]
        left = self.binarySearch(nums, target, True)
        if left != -1:
            results = [left, left]
        right = self.binarySearch(nums, target, False)
        results[1] = right
        return results
