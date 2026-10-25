class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            while(len(prefix) >0 and not strs[i].startswith(prefix)):
                prefix = prefix[:-1]
        return prefix