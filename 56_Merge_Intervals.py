from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        outputs = []
        while len(intervals) >= 2:
            a, b = intervals.pop(0)
            c, d = intervals[0]
            if b < c:
                outputs.append([a, b])
            else:
                intervals.pop(0)
                intervals.insert(0, [a, max(b, d)])
        outputs += intervals
        return outputs


# More simple and efficient
class SolutionV2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda interval: interval[0])
        outputs = []
        left, right = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= right:
                right = max(right, intervals[i][1])
            else:
                outputs.append([left, right])
                left, right = intervals[i]
        outputs.append([left, right])
        return outputs
