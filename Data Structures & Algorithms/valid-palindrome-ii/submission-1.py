class Solution:
    def validPal(self,s: str) -> bool:
        low1 = 0
        high1 = len(s) -1
        while low1 < high1:
            if s[low1] != s[high1]:
                return False
            low1 += 1
            high1 -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s) -1
        
        while low<high:
            if s[low] != s[high]:
                return (self.validPal(s[low+1:high+1]) or self.validPal(s[low:high]))
            low +=1
            high -=1
        return True


    