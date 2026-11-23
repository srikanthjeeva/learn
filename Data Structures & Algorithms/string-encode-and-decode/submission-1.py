class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for i in strs:
            output += str(len(i)) + "#" + i

        return output

    def decode(self, st: str) -> List[str]:
        output = []
        i = 0
        while i < len(st):
            j = i
            while st[j] != "#":
                j+=1
            
            #i=int, j=#
            lengthofst = int(st[i:j])
            i=j+1
            j=i+lengthofst

            output.append(st[i:j])
            i=j

        return output
