from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 0:
            return [1]
        prev_half = [1]
        current_half = []
        for i in range(1, rowIndex + 1):
            current_half = []
            if i % 2 == 0:
                prev_half.append(prev_half[-1])
            num_half = (i + 2) // 2
            for j in range(num_half):
                if j == 0:
                    current_half.append(1)
                else:
                    current_half.append(prev_half[j - 1] + prev_half[j])
            prev_half = current_half
        reverse = None
        if (rowIndex + 1) % 2 == 0:
            reverse = [current_half[i] for i in range(len(current_half) - 1, -1, -1)]
        else:
            reverse = [current_half[i] for i in range(len(current_half) - 2, -1, -1)]
        result = current_half + reverse
        return result


