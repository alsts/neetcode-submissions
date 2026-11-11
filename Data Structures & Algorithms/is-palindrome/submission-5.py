class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            
            # cleanup
            while l < r and not s[l].isalnum(): # remove non alnum chars left side
                l += 1
            while l < r and not s[r].isalnum(): # remove non alnum chars right side
                r -= 1    

            # main check
            if s[l].lower() != s[r].lower(): # if not equal on both side -> invalid palindrome
                return False

            l += 1
            r -= 1    
        
        return True