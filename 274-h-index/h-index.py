class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                return len(citations) - i
        
        return 0  # If no H-Index is found
