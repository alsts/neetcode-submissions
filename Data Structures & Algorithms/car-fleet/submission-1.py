class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets_stack = [] # closer to target added first, reversed

        for p, s in sorted( zip(position, speed) , reverse=True):
            t = (target - p) / s # time to reach target alone
            fleets_stack.append(t) 
            if len(fleets_stack) >= 2 and fleets_stack[-1] <= fleets_stack[-2]:
                # catches the slower car with higher position -> merge
                fleets_stack.pop()


        return len(fleets_stack) # number of fleets