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



