class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have = 0
        res, res_len = [-1, -1], float("infinity")

        l, r = 0, 0
        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # needed char count
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # found:
            while have == len(count_t):
                # update result if smaller:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                
                # pop window from left:
                window[s[l]] -= 1

                # check less than needed char count
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

            r += 1

        return s[res[0] : res[1] + 1] if res_len > 0 else ""
        