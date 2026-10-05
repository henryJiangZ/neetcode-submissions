class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                stack.append(s[i])
            elif (s[i] == "}" or s[i] == "]" or s[i] == ")") and len(stack) == 0:
                return False
            elif len(stack) == 0:
                return True
            elif (stack[-1] == "{" and s[i] == "}") or (stack[-1] == "(" and s[i] == ")") or (stack[-1] == "[" and s[i] == "]"):
                stack.pop()
            else:
                return False
        if len(stack) >0:
            return False
        return True

            