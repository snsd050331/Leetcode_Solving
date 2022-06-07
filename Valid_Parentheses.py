class Solution:
    def isValid(self, s: str) -> bool:
        checkdict = {"(" : ")", "[" : "]", "{" : "}"}
        stack = []
        for i in s:
            if i in checkdict.keys():
                stack.append(checkdict[i])
            elif not len(stack) == 0 and stack.pop(-1) == i:
                pass
            else:
                return False
        return len(stack) == 0

        
if __name__ == '__main__':
    s = "()" # Output: true
    # s = "()[]{}" # Output: true
    # s = "(]" # Output: false
    P1 = Solution().isValid(s)