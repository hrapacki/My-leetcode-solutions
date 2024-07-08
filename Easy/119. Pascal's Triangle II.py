class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = []
        c=  []
        for x in range(rowIndex+1):
            b = []
            for y in range(x + 1):
                if y == 0 or y == x:
                    b.append(1)
                else:
                    b.append(a[x-1][y-1] + a[x-1][y])
            a.append(b)
            c = b
        return c