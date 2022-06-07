class Solution:
    def removeDuplicates(self, nums: list):
        Index = 0
        for i in range(1, len(nums)):
            if nums[Index] != nums[i]:
                Index += 1
                nums[Index] = nums[i]
        return Index + 1
            
        
if __name__ == '__main__':
    # nums = [1,1,2] # Output: 2, nums = [1,2,_]
    nums = [0,0,1,1,1,2,2,3,3,4] # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    P1 = Solution().removeDuplicates(nums)