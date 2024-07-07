class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        l = list(s)
        for x in range (len(l)):
            match l[x]:
                case "I":
                    val = val+1
                case "V":
                    if l[x-1] == "I"and x>0:
                        val = val + 3
                    else:
                        val = val + 5
                case "X":
                    if l[x-1] == "I"and x>0:
                        val = val + 8
                    else:
                        val = val + 10
                case "L":
                    if l[x-1] == "X"and x>0:
                        val = val + 30
                    else:
                        val = val + 50
                case "C":
                    if l[x-1] == "X"and x>0:
                        val = val + 80
                    else:
                        val = val + 100
                case "D":
                    if l[x-1] == "C"and x>0:
                        val = val + 300
                    else:
                        val = val + 500
                case "M":
                    if l[x-1] == "C" and x>0:
                        val = val + 800
                    else:
                        val = val + 1000
        return val
