class Solution:
    def lengthOfLastWord(self, s):
        s = s.strip()
        num = len(s.split(' ')[-1])
        return num

if __name__ == '__main__':
    # s = "Hello World"                     # Output: 5
    s = "   fly me   to   the moon  "     # Output: 4
    # s = "luffy is still joyboy"           # Output: 6
    P1 = Solution().lengthOfLastWord(s)