class Solution:
    def climbStairs(self, n):
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        return cur       
        
if __name__ == '__main__':
    n = 6 # Output: 2
    # n = 3 # Output: 3
    P1 = Solution().climbStairs(n)
        