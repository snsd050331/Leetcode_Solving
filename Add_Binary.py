class Solution:
    def addBinary(self, a, b):
        num = bin(int(a, 2) + int(b, 2))[2:]
        return num
        
if __name__ == '__main__':
    # a = "11"
    # b = "1"       # Output: "100"
    
    a = "1010"
    b = "1011"    # Output: "10101"
    P1 = Solution().addBinary(a, b)