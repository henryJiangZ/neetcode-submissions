class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        past = {}
        for word in strs:
            anagram = {}
            for char in word:
                if char not in anagram:
                    anagram[char] = 1
                else:
                    anagram[char] += 1
            aTuple = tuple(sorted(anagram.items()))
            if aTuple not in past:
                past[aTuple] = [word]
            else:
                past[aTuple].append(word)
        for item in past.values():
            group.append(item)
            
        return group