class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = ""
        while columnNumber > 0:
            columnNumber -= 1
            col = chr(columnNumber % 26 + 65) + col
            columnNumber //= 26
        return col
