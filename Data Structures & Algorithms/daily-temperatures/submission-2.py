class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            
            # check if temp is warmer than top of stack
            while len(stack) > 0 and t > stack[-1][1]:
                prev_temp = stack.pop()
                res[prev_temp[0]] = i - prev_temp[0] # diff to temp position, days till warmer

            stack.append((i, t))

        return res


