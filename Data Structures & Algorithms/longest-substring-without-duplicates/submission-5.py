class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        max_seq = 0
        buffer = set()
        l, r = 0, 0

        while r < len(s):

            while s[r] in buffer: # duplicate, s[r] must be added, loop until exists in set
                buffer.remove(s[l])
                l += 1

            buffer.add(s[r])
            max_seq = max(max_seq, r - l + 1)

            r += 1

        return max_seq    
