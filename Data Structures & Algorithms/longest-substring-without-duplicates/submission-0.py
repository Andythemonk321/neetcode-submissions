class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()
        n = len(s)

        for i in range(n):
            while s[i] in sett:
                sett.remove(s[l])
                l += 1

            w = (i - l) + 1

            longest = max(longest, w)

            sett.add(s[i])

        return longest

        