from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            tmp = nums1
            nums1 = nums2
            nums2 = tmp
        total_len = len(nums1) + len(nums2)
        if total_len == 1:
            return float(nums2[0])
        half_len = int((total_len + 1) / 2)
        start_1, end_1 = 0, len(nums1)

        while start_1 <= end_1:
            i = int((start_1 + end_1) / 2)
            j = half_len - i

            if i > 0 and nums1[i - 1] > nums2[j]:
                end_1 = i - 1
            elif i < len(nums1) and nums2[j - 1] > nums1[i]:
                start_1 = i + 1
            else:
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if i == len(nums1):
                    min_right = nums2[j]
                elif j == len(nums2):
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                if total_len % 2 == 1:
                    return float(max_left)
                else:
                    return (max_left + min_right) / 2

        return 0.0
