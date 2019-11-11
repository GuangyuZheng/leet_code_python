class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        size = min(height[left], height[right]) * (right - left)
        while left < right:
            tmp_size = min(height[left], height[right]) * (right - left)
            size = max(size, tmp_size)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return size
