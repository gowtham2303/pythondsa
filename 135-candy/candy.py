class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        #here we intialise two arrays from right side one and left side one ..
        left_array=[1]*len(ratings)
        right_array=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                left_array[i]=left_array[i-1]+1
            else :
                left_array[i]=1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right_array[i]=right_array[i+1]+1
            else :
                right_array[i]=1
        
        for i in range(len(ratings)):
            left_array[i]=max(left_array[i],right_array[i])
        
        return sum(left_array)

            
