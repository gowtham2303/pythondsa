class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy =0
        for i in range(1,len(prices)):
            max_profit = max(max_profit , prices[i]-prices[buy])
            if prices[i]<prices[buy]:
                buy=i
        return max_profit


