class Solution:

    def encode(self, strs: List[str]) -> str:
        temp = []
        for i in strs:
            m = len(i)
            i = str(m) + '#' + i  #concat karva + use thay
            temp.append(i)

        s = ''.join(temp) #join() ne string separator sathe call karvanu hoy. ahiya '' means koi separator nai
        return s    

    def decode(self, s: str) -> List[str]:
        temp = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != '#':
                length += s[i]
                i += 1

            length = int(length)

            i += 1

            word = ""    
            for j in range(length):
                word += s[i]
                i += 1
                   
            temp.append(word)

        return temp             
