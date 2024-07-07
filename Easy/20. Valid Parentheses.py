class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2==1):
            return False
        counter = 0
        opened = []
        l = list(s)
        for x in range(len(s)):
            match l[x]:
                case "(":
                    opened.append("(")
                    counter += 1
                case ")":
                    if counter>0:
                        prev = opened.pop()
                    else:
                        return False
                    if prev == "(" :
                        counter -= 1
                    else:
                        return False
                case "[":
                    opened.append("[")
                    counter += 1
                case "]":
                    if counter>0:
                        prev = opened.pop()
                    else:
                        return False
                    if  prev  == "[":
                        counter -= 1
                    else:
                        return False
                case "{":
                    opened.append("{")
                    counter += 1
                case "}":
                    if counter>0:
                        prev = opened.pop()
                    else:
                        return False
                    if prev == "{":
                        counter -= 1
                    else:
                        return False
        if counter != 0:
            return False         
        return True

