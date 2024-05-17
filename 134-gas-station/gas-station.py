class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        trip_tank =0
        curr_tank=0
        start =0
        for i in range(len(gas)):
            trip_tank +=gas[i]-cost[i]
            curr_tank +=gas[i]-cost[i]
            if curr_tank<0:
                start=i+1
                curr_tank=0
        return start if trip_tank>=0 else -1