class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = defaultdict(list)

        for s in strs:
            anagrams_groups["".join(sorted(s))].append(s)

        
        return list(anagrams_groups.values())