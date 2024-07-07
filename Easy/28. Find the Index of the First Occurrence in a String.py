class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        key = list(needle)
        string = list(haystack)
        found = -1
        if len(key) > len(string):
            return found
        for x in range(len(string)):
            if found != -1:
                break
            if key[0] == string[x]:
                found = x
                for y in range(1, len(key)):
                    if x+len(key) > len(string):
                        found = -1
                        break
                    if key[y] != string[x + y]:
                        found = -1
                        break
        return found