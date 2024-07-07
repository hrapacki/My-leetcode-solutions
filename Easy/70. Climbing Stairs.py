import math
class Solution:
    def climbStairs(self, n: int) -> int:
        comb = 1
        max_num_of_twos = n // 2
        for x in range (1,max_num_of_twos+1):
            how_many_ones = n - x*2
            comb += (math.factorial(how_many_ones+x))/(math.factorial(x)*math.factorial(how_many_ones))
        comb = int(comb)
        return comb
