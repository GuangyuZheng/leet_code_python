from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        m_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                m_profit += prices[i] - prices[i-1]
        return m_profit
