class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            word_len = int(s[i:j])
            i = j + 1  # beginning of word
            j = i + word_len  # end of word
            decoded.append(s[i:j])

            i = j

        return decoded
                    
    