class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        past = {}
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char.lower())-ord('a')] += 1
            aTuple = tuple(count)
            if aTuple not in past:
                past[aTuple] = [word]
            else:
                past[aTuple].append(word)
        for item in past.values():
            group.append(item)
        return group