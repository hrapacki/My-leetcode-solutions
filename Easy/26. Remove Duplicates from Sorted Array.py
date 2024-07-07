class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        to_replace = []
        counter = 1
        if len(nums) == 1:
            return counter
        for x in range (1, len(nums)):
            prev = nums[x-1]
            print (x)
            if prev == nums[0] and prev != nums[x] and len(nums)==2:
                counter+=1
            if nums[x] == prev:
                print ("y")
                to_replace.append(x)
                print(to_replace[0])
            if nums[x] != prev:
                counter+=1
                if len(to_replace)>0:
                    nums[to_replace.pop(0)]=nums[x]
                    to_replace.append(x)
        return counter

            