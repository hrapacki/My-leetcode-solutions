#o(n) complexity, much faster
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = 100001
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit


#much slower, first version with O(n^2) complexity, thus reaching the time limit in tests:
""" class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        max_diff=0
        max_diff_old=0
        for z in range(len(prices)):
            max = prices[0]
            x_pos = 0
            for x in range (len(prices)):
                if prices[x] > max:
                    max = prices[x]
                    x_pos = x
            min = prices[x_pos]
            if x_pos==0:
                min = max
            else:
                for y in range (x_pos,-1,-1):
                    if prices[y]<min and prices[y]!=-1:
                        min=prices[y]
            max_diff=max-min
            print(max,min)
            prices[x_pos] = -1
            if max_diff_old < max_diff:
                max_diff_old=max_diff
        return max_diff_old """
        
