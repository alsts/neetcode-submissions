class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []

        for i, word in enumerate(strs):
            word_chars = self.helper(word)

            if not self.helper2(anagrams, word, word_chars):
                anagrams.append([word])

        return anagrams

    def helper2(self, anagrams, word, word_chars):
        for an_group in anagrams:
            an_group_word = an_group[0]

            if len(word) != len(an_group_word):
                continue

            an_group_word_chars = self.helper(an_group_word)

            if an_group_word_chars == word_chars:
                an_group.append(word)
                return True

    def helper(self, word):
        word_chars = {}
        for j, char in enumerate(word):
            word_chars[char] = 1 + word_chars.get(char, 0)
        return word_chars
        