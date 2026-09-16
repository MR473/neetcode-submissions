class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))
            encoded_string += '@'
            encoded_string += s
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        n = ""
        decoded_string = []

        if s == None:
            return []
        else:
            while len(s) != 0:
                n += s[i]
                i += 1
                if s[i] == '@':
                    decoded_string.append(s[i+1:i+int(n)+1])
                    s = s[i+int(n)+1:]
                    i = 0
                    n = ""
            return decoded_string

