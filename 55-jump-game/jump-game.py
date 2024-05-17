class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        
        last_index = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):  # Start from second to last index
            if nums[i] + i >= last_index:
                last_index = i
        
        return last_index == 0
