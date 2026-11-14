class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        close_to_open = {'}': '{', ')': '(', ']': '['}

        for c in s:
            if c in close_to_open:
                if len(stack) > 0 and stack[-1] == close_to_open[c]: # matching closing bracket found
                    stack.pop()
                else:
                    return False # missing or different type of bracket
            else:
                stack.append(c)  
        
        return len(stack) == 0