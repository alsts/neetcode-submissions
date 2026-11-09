class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for l in s:
                pos = ord(l) - ord('a')
                key[pos] += 1

            anagrams_groups[tuple(key)].append(s)

        
        return list(anagrams_groups.values())