class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count, window = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[(ord(s1[i]) - ord('a'))] += 1
            window[(ord(s2[i]) - ord('a'))] += 1
        
        if s1_count == window:
            return True

        for r in range(len(s1), len(s2)):
            window[ord(s2[r]) - ord('a')] += 1 # char entering
            window[ord(s2[r - len(s1)]) - ord('a')] -= 1 # char leaving r - len of s1

            if s1_count == window:
                return True


        return False