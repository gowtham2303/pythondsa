class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss=s.strip()
        list=ss.split(" ")
        return len(list[-1])
