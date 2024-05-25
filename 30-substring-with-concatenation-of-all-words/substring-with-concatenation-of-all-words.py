class Solution:
    def findSubstring(self, s, words) :
        wslen, wlen = len(words), len(words[0])
        words, res = Counter(words), []
        for i in range(0, len(s) - wslen*wlen + 1):
            hmap = words.copy()
            for j in range(i, i + wslen*wlen, wlen):
                if not hmap[s[j:j + wlen]]:
                    break
                hmap[s[j:j + wlen]] -= 1
            if not any(hmap.values()):
                res.append(i)
        return res