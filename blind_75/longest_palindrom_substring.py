#https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        palindrome = s[0]
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(palindrome):
                    palindrome = s[i:j]
        return palindrome


class SolutionExpansionOverMiddle:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        def expand_over_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left+1: right]

        palindrome = s[0]
        for i in range(len(s)):
            odd_length_palindrome = expand_over_center(i, i)
            even_length_palindrome = expand_over_center(i, i+1)
            if len(odd_length_palindrome) > len(palindrome):
                palindrome = odd_length_palindrome
            if len(even_length_palindrome) > len(palindrome):
                palindrome = even_length_palindrome
        return palindrome
