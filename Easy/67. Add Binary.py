class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l1 = list(a)
        l2 = list(b)
        num1 = 0
        num2 = 0
        num3 = 0
        for x in range (len(l1)):
            if l1[x] == "1":
                num1 = num1 + 2**(len(l1)-1-x)
        for x in range (len(l2)):
            if l2[x] == "1":
                num2 = num2 + 2**(len(l2)-1-x)
        num3 = num1+num2
        return bin (num3)[2:]