class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # top of stack is higher temp:
            while stack and t > stack[-1][1]:
                temp = stack.pop()
                res[temp[0]] = i - temp[0] # distance to item that is higher
            
            stack.append((i, t))
        
        return res


