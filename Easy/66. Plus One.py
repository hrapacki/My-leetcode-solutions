from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        x = 1
        if digits[len(digits)-x] == 10:
            digits[len(digits)-x] = 0
            if len(digits)-x == 0:
                digits[len(digits)-x] = 1
                digits.append(0)
            else:
                found_spot = False
                x = 2
                skipped = 0
                while found_spot == False:
                    if digits[len(digits)-x] < 9:
                        digits[len(digits)-x] += 1
                        found_spot = True
                        if skipped > 0:
                            while skipped !=0:
                                print(len(digits)-x+skipped)
                                digits[len(digits)-x+skipped]=0
                                skipped -= 1
                        break
                    else:
                        skipped +=1
                    if len(digits)-x == 0 and digits[len(digits)-x] == 9:
                        print (x)
                        print ("a")
                        digits[0] = 1
                        for x in range(1, len(digits)):
                            digits[x] = 0
                        digits.append(0)
                        found_spot = True
                    x += 1
        return digits