class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        nums=prices
        profits=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>0:
                profits+=nums[i]-nums[i-1]
        return profits



     









        profit = 0
        for i in range (1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit 