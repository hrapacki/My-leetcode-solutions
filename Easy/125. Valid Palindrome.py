#Need to come back later to optimalize the algorithm, works, but too slow

class Solution:
    def isPalindrome(self, s: str) -> bool:
        to_check = list(s)
        alphanumeric = []
        for x in range (len(s)):
            if (ord(to_check[x])>47 and ord(to_check[x]) < 58) or (ord(to_check[x])>64 and ord(to_check[x]) < 91) or (ord(to_check[x])>96 and ord(to_check[x]) < 123):
                alphanumeric.append(to_check[x])
        print(alphanumeric)
        for x in range (len(alphanumeric)//2):
            if ord(alphanumeric[x]) != ord(alphanumeric[len(alphanumeric)-1-x]) and ord(alphanumeric[x]) != ord(alphanumeric[len(alphanumeric)-1-x])-32 and ord(alphanumeric[x])-32 != ord(alphanumeric[len(alphanumeric)-1-x]):
                return False
            if ord(alphanumeric[x])<58 and ord(alphanumeric[len(alphanumeric)-1-x])-32>25 or ord(alphanumeric[x])>57 and ord(alphanumeric[len(alphanumeric)-1-x])-32<26: 
                return False
        print(alphanumeric)
        return True
