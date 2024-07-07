class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        reverse = 0
        normal = x
        while x > 0:
            addDigit = x%10
            reverse = reverse * 10 + addDigit
            x = x//10
        return normal == reverse
