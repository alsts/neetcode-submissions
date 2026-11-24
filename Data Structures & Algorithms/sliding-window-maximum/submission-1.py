class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):

            # 1, 1, 1, 1, 4 -> only keep 4 in window
            # 8, 7, 6, 9 -> k = 2
            # [8, 7], [7, 6], [6], [] (pop), [9]
            # [8, 7, 6] -> 10 -> [] -> [10]

            # if top of queue smaller than current number -> remove:
            # keeps condition of monotonic decreasing queue:
            while q and nums[r] > nums[q[-1]]:
                q.pop() # pop from right

            q.append(r)    

            # remove left from window -> out of bounds window
            if l > q[0]:
               q.popleft() 
           
            # window is grown
            if (r + 1) >= k:
                output.append(nums[q[0]]) # left most is max
                l += 1
            
            r += 1
        
        return output