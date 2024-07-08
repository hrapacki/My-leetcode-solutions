#Low memory usage but very high runtime need to optimize
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a=0
        found = False
        while len(nums)>1 and found == False: 
            for z in range(len(nums)-1,0,-1):
                if len(nums)==1:
                    break
                if nums[z] == nums[0] and z!=0:
                    nums.pop(0)
                    nums.pop(z-1)
                    break
                elif nums[0]!=nums[z] and z==1:
                    found = True
                    return nums[0]
        return nums[0]