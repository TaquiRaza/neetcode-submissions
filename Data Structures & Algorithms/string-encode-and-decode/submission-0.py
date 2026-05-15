class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + '#' + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find delimj
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            result.append(s[j+1:j+1+word_len])
            i = j + 1 + word_len

        return result