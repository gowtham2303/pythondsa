class Solution(object):
    def maxArea(self, height):
        ans=0
        s=0
        e=len(height)-1
        while s<e:
            area=(e-s)*min(height[s],height[e])
            ans=max(area,ans)
            if height[s]<height[e]:
                s+=1
            else:
                e-=1
        return ans
        # for i in range(len(height)):
        #     y1=height[i]
        #     for j in range(i+1,len(height)):
        #         y2=height[j]
        #         x2=j-i
        #         length=min(y1,y2)
        #         area=length*x2
        #         ans=max(ans,area)
        # return ans
    
        