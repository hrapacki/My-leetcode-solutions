class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        counter = 0
        common = ""
        if(len(strs)==1):
            return strs[0]
        maxCom = strs[0]
        for x in range (len(strs)):
            if len(maxCom) > len(strs[x]):
                maxCom = strs[x]
        check = strs[0]
        while counter <= len(maxCom)-1: #the longest common prefix can't be longer than the shortest word
            for x in range (1, len(strs)): #check if the letter on position counter is the same in every word, then move to next position until maxCom
                next = strs[x]
                if check[counter] == next[counter]:
                    if x == len(strs)-1:
                        common = common + check[counter]
                        counter += 1
                else:
                    counter = len(maxCom)
                    break
        return (common)