class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        window = {}

        # fill s1 freq
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1
        
        # slide through s2
        l, r = 0, 0
        while r < len(s2):

            # window outgrew s2 -> shrink
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1

            # update window
            window[s2[r]] = window.get(s2[r], 0) + 1

            if freq1 == window:
                return True

            r +=1
        
        return False