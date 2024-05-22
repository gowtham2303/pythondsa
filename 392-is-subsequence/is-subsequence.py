class Solution:
    def isSubsequence(self, s, t):
        sub_pivot = 0
        str_pivot = 0
        
        while sub_pivot < len(s) and str_pivot < len(t):
            if s[sub_pivot] == t[str_pivot]:
                sub_pivot += 1
            str_pivot += 1
        
        return False if sub_pivot < len(s) else True
        