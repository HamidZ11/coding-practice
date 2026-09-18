class Solution:
    def longestRun(self, source: str) -> str:

        current_run = 1
        max_run = 1
        max_char = source[-1]

        for i in range(1, len(source)):
            if source[i] == source[i-1]:
                current_run += 1

                if current_run >= max_run:
                    max_run = current_run
                    max_char = source[i]
            else:
                current_run = 1
            

        return max_char + str(max_run)
            




s = Solution()

print(s.longestRun("bbacccdbbab"))  # expected: c3
print(s.longestRun("aabbcc"))       # expected: c2
print(s.longestRun("zzzz"))         # expected: z4
print(s.longestRun("abc"))          # expected: c1
print(s.longestRun("aaabbbaaa"))    # expected: a3
print(s.longestRun("x"))            # expected: x1

print(s.longestRun("aaaabcc"))        # expected: a4
print(s.longestRun("abbbcc"))         # expected: b3
print(s.longestRun("aabbbaa"))        # expected: b3
print(s.longestRun("aaabbbccc"))      # expected: c3
print(s.longestRun("aabbaa"))         # expected: a2
print(s.longestRun("mmmmnnnmmmm"))    # expected: m4
print(s.longestRun("ppqqqrrrsss"))    # expected: s3
print(s.longestRun("abcdefg"))        # expected: g1
print(s.longestRun("aaaaa"))          # expected: a5
print(s.longestRun("abbba"))          # expected: b3