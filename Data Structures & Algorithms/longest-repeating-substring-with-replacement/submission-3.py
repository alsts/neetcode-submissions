class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_window = 0
        counts = {}

        while r < len(s):
            # count char
            counts[s[r]] = counts.get(s[r], 0) + 1   

            # VALID WINDOW: AAA[k replacements] -> AAAAA
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                if counts[s[l]] == 0:
                    del counts[s[l]]
                l += 1

             
            max_window = max(max_window, (r - l + 1))
            r +=1

        return max_window

