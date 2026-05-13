class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minB = prices[0]
        for sellP in prices:
            profit = sellP - minB
            maxP = max(maxP, profit)
            minB = min(minB, sellP)
        return maxP


        

        
        