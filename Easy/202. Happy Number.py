class Solution:
    def isHappy(self, n: int) -> bool:
        search_list = []
        found = False
        num = n
        sum = 0
        z = 0
        found_sums = []
        while not found:
            sum = 0
            while num>9:
                search_list.append(num%10)
                num = num//10
            search_list.append(num%10)
            for x in range(len(search_list)):
                search_list[x] *= search_list[x]
                sum += search_list[x]
            found_sums.append(sum)
            for x in range (len(found_sums)-1):
                if sum == found_sums[x]:
                    return False
                    break
            if sum == 1:
                found = True
                return True
            else:
                num = sum
                search_list.clear()
                z+=1
        return False