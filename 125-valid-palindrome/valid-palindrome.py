class Solution(object):
    def isPalindrome(self, s):
        characters=[char.lower() for char in s if char.isalnum()]
        return characters==characters[::-1] 
