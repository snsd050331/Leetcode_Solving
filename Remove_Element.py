class Solution:
    def removeElement(self, nums, val):
        Index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[Index] = nums[i]
                Index += 1
        return Index
if __name__ == '__main__':
    # nums = [3,2,2,3]
    # val = 3            # Output: 2, nums = [2,2,_,_]
    nums = [0,1,2,2,3,0,4,2]
    val = 2            # Output: 5, nums = [0,1,4,0,3,_,_,_]    
    P1 = Solution().removeElement(nums, val)