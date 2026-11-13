class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0 , 1
        char_set = set()
        max_seq = 0

        for r in range(len(s)):

            # cleanup duplicate chars
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            max_seq = max(max_seq, r - l + 1)
        
        return max_seq

