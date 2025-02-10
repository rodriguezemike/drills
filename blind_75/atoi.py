#https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "" or s.startswith("+-") or s.startswith("-+") or s.startswith("++") or s.startswith("--"):
            return 0
        res = ""
        sign = -1 if s[0] == "-" else 1
        s = s.lstrip("-").lstrip("+").lstrip("0")
        for i in range(0, len(s)):
            if not s[i].isnumeric():
                break
            res += s[i]
        res = int(res) if res else 0
        res = sign * res
        if res < -2**31:
            res = -2**31
        elif res > 2**31 - 1:
            res = 2**31 - 1
        return res
