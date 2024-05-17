class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        farthest =0
        jumps=0
        current =0 
        for i in range(len(nums)-1):

            
            farthest = max (farthest ,nums[i]+i)

            if current == i :
                current = farthest 
                jumps+=1
        return jumps