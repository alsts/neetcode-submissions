class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # 26 possible characters - only lowercase English letters
            letters_count = [0 for i in range(0, 26)]  # a

            for letter in word:
                letter_slot = ord(letter) - ord('a')
                letters_count[letter_slot] += 1

            anagrams[tuple(letters_count)].append(word)

        return list(anagrams.values())
        