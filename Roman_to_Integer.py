class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        total_val = 0
        last_val = 0
        current_val = 0
        
        while s:
            current_val = r2i[s[-1]]
            s = s[:-1]
            if current_val >= last_val:
                total_val += current_val
            else:
                total_val -= current_val
            
            last_val = current_val
        return total_val

if __name__ == '__main__':
    s1 = "III" #3
    P1 = Solution().romanToInt(s1)
    print(P1)
    
    s2 = "LVIII" #58
    P2 = Solution().romanToInt(s2)
    print(P2)
    
    s3 = "MCMXCIV" #1994
    P3 = Solution().romanToInt(s3)
    print(P3)
    