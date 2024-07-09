class Solution:
    def reverseBits(self, n: int) -> int:
        a=list("{:032b}".format(n))
        print(a)
        for x in range(16):
            if a[x] != a[31-x]:
                temp = a[x]
                a[x] = a[31-x]
                a[31-x]=temp
        return int(''.join(a), 2)