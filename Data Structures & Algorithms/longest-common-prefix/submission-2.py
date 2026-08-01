class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for s in strs:
            sdict = {}
            for index,char in enumerate(s):
                sdict[index] = char
        
        prefix = strs[0]
        for word in strs[1:]:
            while word.startswith(prefix) != True and len(prefix) > 0:
                prefix = prefix[:-1]
            if prefix == "":
                return ""
        return prefix