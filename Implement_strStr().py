class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)
if __name__ == '__main__':
    # haystack = "hello"
    # needle = "ll"               # Output: 2
    haystack = "aaaaa"
    needle = "bba"              #Output: -1
    
    P1 = Solution().strStr(haystack, needle)