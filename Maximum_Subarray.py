class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
            res = max(res, nums[i])
        return res

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4] # Output: 6
    # nums = [1]                     # Output: 1
    # nums = [5,4,-1,7,8]            # Output: 23
    P1 = Solution().maxSubArray(nums)