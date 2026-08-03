class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyP = prices[0]
        sellP = prices[0]
        res = 0
        for sellP in prices:
            res = max(res, sellP - buyP)
            if sellP < buyP:
                buyP = sellP
        return res