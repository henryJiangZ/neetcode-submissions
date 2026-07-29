class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        scount = {}
        tcount = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            scount[s[i]] = s.count(s[i])
            tcount[s[i]] = t.count(s[i])

        for i in range(len(s)):
            if scount[s[i]]!=tcount[s[i]]:
                return False
        return True