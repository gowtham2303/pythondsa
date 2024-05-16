class Solution(object):
    def rotate(self, nums, k):
        num = nums[:]
        start=0
        for i in range(len(nums)):
            nums[(i+k)%len(nums)]=num[i]
       



