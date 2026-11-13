class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l, r = 0, 0
        char_set = set()

        while r < len(s):
            while s[r] in char_set: # duplicate found -> remove until not present
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, len(char_set))
            r += 1

        return res

