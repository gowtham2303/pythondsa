class Solution(object):
    def rotate(self, nums, k):
        # num = nums[:]
        # start=0
        # for i in range(len(nums)):
        #     nums[(i+k)%len(nums)]=num[i]


        
        k = k % len(nums)
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])


