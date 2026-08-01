class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            if prefix == "":
                    return ""
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix