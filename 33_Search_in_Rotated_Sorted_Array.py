from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find pivot
        if len(nums) == 0:
            return -1
        if nums[0] <= nums[len(nums) - 1]:
            pivot = 0
        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    break
                else:
                    if nums[mid] >= nums[left]:
                        left = mid + 1
                    else:
                        right = mid - 1
            pivot = (left + right) // 2 + 1

        vleft, vright = 0, len(nums) - 1
        while vleft <= vright:
            vmid = (vleft + vright) // 2
            tmid = (vmid + pivot) % len(nums)
            if nums[tmid] == target:
                return tmid
            elif nums[tmid] < target:
                vleft = vmid+1
            else:
                vright = vmid-1
        return -1


# Treat the rotated array as two sorted array
class SolutionV2:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (target >= nums[0]) == (nums[mid] >= nums[0]):
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = -10e10
                else:
                    num = 10e10
            if num > target:
                hi = mid - 1
            elif num < target:
                lo = mid + 1
            else:
                return mid
        return -1


# If we split the rotated array, at least there exists one sorted array
# [4 5 6 7 1 2 3] split at 7 -> [4 5 6 7] [7 1 2 3]
# If target in the sorted array, then discard the the rest part, vise versa
class SolutionV3:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start, end = 0, n-1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1
