class Solution(object):
    def threeSum(self, nums ):
        res = []
        
        dup_set = set()
        nums.sort()
        
        for i in range(len(nums)):
            target = -nums[i]
            l,r = i+1,len(nums)-1
            while l < r:
                val = nums[l] + nums[r]
                if val == target and (nums[l],nums[r]) not in dup_set:
                    res.append([nums[i],nums[l],nums[r]])
                    dup_set.add((nums[l],nums[r]))
                if val > target:
                    r -= 1
                else:
                    l+=1
        return res