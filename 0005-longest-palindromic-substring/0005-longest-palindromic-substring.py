class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        max_pel_str = ''
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > max_length:
                    max_pel_str = s[i:j]
                    max_length = len(s[i:j])
        return max_pel_str