class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_window = 0
        counts = {}

        while r < len(s):
            # add char first
            counts[s[r]] = counts.get(s[r], 0) + 1
            
            # shrink until condition matches -> [ window - max(chars count) <= k (to replace) ]
            max_char_count = max(counts.values())
            while (r - l + 1) - max_char_count > k:
                counts[s[l]] -= 1
                l += 1

            max_window = max(max_window, (r - l + 1))
            r += 1

        return max_window

