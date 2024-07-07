class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = list(s)
        letter_found = False
        space_found = False
        length = 0
        x = len(text)-1
        while space_found == False and x >= 0:
            if text[x].isspace()==False:
                length+=1
                while space_found == False and x > 0:
                    x-=1
                    print (x)
                    if text[x].isspace()==False and len(text)>1:
                        length+=1
                    else:
                        space_found = True
                        return length   
            x-=1
        return length