class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        for y in range (1,x):
            if y*y == x:
                return y
            if y*y > x:
                return y-1
        return 1