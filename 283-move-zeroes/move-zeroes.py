class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        right=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[right]=nums[i]
                right+=1
        for i in range(right,len(nums)):
            nums[i]=0