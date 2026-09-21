class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        past = {}
        for index,word in enumerate(strs):
            seen = {}
            for char in word:
                if char not in seen:
                    seen[char] = 1
                elif char in seen:
                    seen[char] = seen[char] +1
            anagram = tuple(sorted(seen.items()))
            if anagram not in past:
                past[anagram] = [word]
            else:
                past[anagram].append(word)

        return list(past.values())
                
            


            
            
                
