class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = defaultdict(list)

        for s in strs:
            letters = [0] * 26

            for l in s:
                pos = ord('z') - ord(l)
                letters[pos] += 1
            
            anagrams_groups[tuple(letters)].append(s)

        
        return list(anagrams_groups.values())