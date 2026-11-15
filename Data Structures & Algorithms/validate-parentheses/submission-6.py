class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        to_open_bracket = {"}": "{","]": "[", ")": "("}

        for c in s:
            if c in to_open_bracket:
                if len(stack) > 0 and stack[-1] == to_open_bracket[c]:
                    stack.pop()
                else:    
                    return False
            else:        
                stack.append(c)

        return len(stack) == 0