class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
                
        
if __name__ == '__main__':
    strs = ["flower","flow","flight"] # Output: "fl"
    # strs = ["dog","racecar","car"] # Output: ""
    P1 = Solution().longestCommonPrefix(strs)