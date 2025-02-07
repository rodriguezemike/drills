#https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        res = -(int(str(x)[::-1][:-1])) if x < 0 else int(str(x)[::-1])
        return res if -(2**31) < res and res <= 2**31 -1 else 0
        
