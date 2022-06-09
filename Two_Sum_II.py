class Solution:
    def twoSum(self, numbers, target):
        N = len(numbers)
        left, right = 0, N-1
        while left < right:
            cursum = numbers[left] + numbers[right]
            if cursum == target:
                return [left + 1, right + 1]
            elif cursum < target:
                left = left + 1
            else:
                right = right - 1
        return [left, right]

if __name__ == '__main__':
    # numbers = [2,7,11,15]
    # target = 9              # Output: [1,2]
    
    numbers = [2,3,4]
    target = 7              # Output: [1,3]
    
    # numbers = [-1,0]
    # target = -1             # Output: [1,2]
    
    P1 = Solution().twoSum(numbers, target)