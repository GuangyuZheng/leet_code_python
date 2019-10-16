from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        min_price = prices[0]
        m_profit = 0
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            m_profit = max(m_profit, prices[i] - min_price)
        return m_profit
