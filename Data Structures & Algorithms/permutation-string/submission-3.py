class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = {}
        window = {}

        for c in s1:
            s1_counts[c] = s1_counts.get(c, 0) + 1

        l, r = 0, 0
        while r < len(s2):

            # move window left side
            if (r - l + 1) > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            window[s2[r]] = window.get(s2[r], 0) + 1
            if window == s1_counts:
                return True

            r += 1

        return False
