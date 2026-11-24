class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):

            # no smaller values exists on queue:
            # keeps condition of monotonic decreasing queue:
            while q and nums[q[-1]] < nums[r]:
                q.pop() # pop from beginning, the 

            q.append(r)    

            # remove left from window
            if l > q[0]:
               q.popleft() 
           
            # window is grown
            if (r + 1) >= k:
                output.append(nums[q[0]]) # left most is max
                l += 1
            
            r += 1
        
        return output