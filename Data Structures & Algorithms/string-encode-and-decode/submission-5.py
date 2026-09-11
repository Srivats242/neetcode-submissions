class Solution:

    def encode(self, strs: List[str]) -> str:
        #for i in range(len(List[str])):
        #for i in range(len(strs)):
           # for j in range(i+1, len(strs)):
                #if((len(str[i]) != len(str[j]))):
                #    str[i] = '#'
                #    str[j] = '*'
                #else:
                  #  str[i] = '^'
                   # str[j] = '^'
        
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
            
    def decode(self, s: str) -> List[str]:
        
        #if(str[i] == '^' and str[j] == '^'):
            #return List[str]
        
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
