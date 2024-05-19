class Solution(object):
    def romanToInt(self, s):
        roman_mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        highest_seen = 0

        for c in reversed(s):

            addition = roman_mapping[c]

            if addition < highest_seen:
                sum -= addition
            else:
                sum += addition
                highest_seen = addition

        return sum
        