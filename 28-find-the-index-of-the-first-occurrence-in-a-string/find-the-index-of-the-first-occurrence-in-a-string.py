class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Handle the edge case where needle is empty
        if not needle:
            return 0
        
        # Get the lengths of needle and haystack
        n_len = len(needle)
        h_len = len(haystack)
        
        # Iterate over haystack with a window the size of needle
        for i in range(h_len ):
            # Check if the substring of haystack matches needle
            if haystack[i:i + n_len] == needle:
                return i
        return -1