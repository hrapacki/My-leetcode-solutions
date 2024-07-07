class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        to_replace = []
        counter = 0
        for x in range(len(nums)):
            if nums [x] == val:
                to_replace.append(x)
            else:
                counter+=1
            if nums[x]!= val and len(to_replace)>0:
                nums[to_replace.pop(0)] = nums[x]
                to_replace.append(x)
        return counter