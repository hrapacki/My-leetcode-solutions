class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for x in range(numRows):
            b = []
            for y in range(x + 1):
                if y == 0 or y == x:
                    b.append(1)
                else:
                    b.append(a[x-1][y-1] + a[x-1][y])
            a.append(b)
        return a
