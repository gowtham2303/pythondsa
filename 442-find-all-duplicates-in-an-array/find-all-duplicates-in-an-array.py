class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        repeat=[]
        single=set()
        for i in range(len(nums)):
            if nums[i] not in single :
                single.add(nums[i])
            else :
                repeat.append(nums[i])
        return repeat
        