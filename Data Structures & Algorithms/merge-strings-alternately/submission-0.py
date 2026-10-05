class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = 0
        j = 0
        for k in range(len(word1)+len(word2)):
            if i >= len(word1):
                merged = merged + word2[j]
                j += 1
            elif j >= len(word2):
                merged = merged + word1[i]
                i +=1
            elif j >= i:
                merged = merged + word1[i]
                i +=1
            else:
                merged = merged + word2[j]
                j +=1
        return merged