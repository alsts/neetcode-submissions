class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_groups = defaultdict(list) # key(tuple of(array 26 letter slots -> count)) -> array of words

        for word in strs:
            # 26 lower case English letters - anagram representation (letter counts)  
            letter_counts = [0] * 26   

            for letter in word:
                letter_slot = ord(letter) - ord("a") # trick to get relative position in range [0 - 26]
                letter_counts[letter_slot] += 1

            anagram_key = tuple(letter_counts) # python magic, can not pass array directly as key for another map
            anagram_groups[anagram_key].append(word)    

        return list(anagram_groups.values())



        