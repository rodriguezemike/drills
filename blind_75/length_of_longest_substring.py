# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq_letters_size = len(set(s))
        length_of_string = len(s)
        if uniq_letters_size < 3 or uniq_letters_size == length_of_string:
            return uniq_letters_size
        length = 3
        for i in range(length_of_string-length):
            for j in range(i+length,length_of_string):
                if len(set(s[i:j+1])) == j - i + 1:
                    length = j - i + 1
                    if length == uniq_letters_size:
                        return length
                else:
                    break
        return length
