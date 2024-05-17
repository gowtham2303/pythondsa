class Solution(object):
    def jump(self, nums):
      
        farthest,jumps,current =0,0,0
 
        for i in range(len(nums)-1):

            
            farthest = max (farthest ,nums[i]+i)

            if current == i :
                current = farthest 
                jumps+=1
        return jumps