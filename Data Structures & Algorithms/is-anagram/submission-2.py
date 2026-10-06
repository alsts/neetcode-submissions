class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for s_str in s:
            s_dict[s_str] = 1 + s_dict.get(s_str, 0)
                    
        for t_str in t:
            t_dict[t_str] = 1 + t_dict.get(t_str, 0)

        return s_dict == t_dict