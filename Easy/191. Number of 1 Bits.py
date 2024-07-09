class Solution:
    def hammingWeight(self, n: int) -> int:
        a=list("{:032b}".format(n))
        count = 0
        for x in range(32):
            if a[x] == '1':
                count+=1
        return count