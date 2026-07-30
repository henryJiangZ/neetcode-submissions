class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        scount = {}
        tcount = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in scount:
                scount[s[i]] +=1
            else:
                scount[s[i]] =1
            if t[i] in tcount:
                tcount[t[i]] +=1
            else:
                tcount[t[i]] = 1

        return tcount == scount