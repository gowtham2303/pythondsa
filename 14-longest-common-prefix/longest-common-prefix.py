class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        prefix=strs[0]
        for word in strs[1:]:
            # Reduce the prefix as needed
            while word[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]

            # If prefix is empty, there's no common prefix
            if not prefix:
                return ""

        return prefix

            
