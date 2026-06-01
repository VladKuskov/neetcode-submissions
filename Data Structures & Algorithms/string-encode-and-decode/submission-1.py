class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            num = s[i:j]
            decoded_strs.append(s[j+1:j+1+int(num)])
            i = j+1+int(num)
        return decoded_strs
