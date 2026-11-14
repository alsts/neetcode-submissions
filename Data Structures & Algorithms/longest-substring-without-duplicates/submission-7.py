class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        max_seq = 0
        l, r = 0, 0
        buffer = set()

        while r < len(s):
            
            # shrink window until duplicate exists:
            while s[r] in buffer:
                buffer.remove(s[l])
                l += 1

            buffer.add(s[r])
            max_seq = max(max_seq, len(buffer))

            r += 1

        return max_seq