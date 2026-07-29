class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        scount = {}
        tcount = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            scount[s[i]] = s.count(s[i])
            tcount[t[i]] = t.count(t[i])

        return tcount == scount