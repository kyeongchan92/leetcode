class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        collect = []
        max_len = 0
        for i, alphabet in enumerate(s):
            if alphabet not in collect:
                collect.append(alphabet)
                max_len = max(max_len, len(collect))
            else:
                restart_idx = len(collect) - 1
                while collect[restart_idx] != alphabet:
                    restart_idx -= 1
                collect = collect[restart_idx+1:] + [alphabet]
        return max_len