class Solution:
    def longestRun(self, source: str) -> str:

        best_char = source[0] 
        best_streak = 0

        current_streak = 0
        current_char = source[0]

        for char in source: 
            if char == current_char: # if your current character is repeated
                current_streak += 1 
            else: 
                current_char = char # now theres a new char because the chars were not equal
                current_streak = 1

            if current_streak >= best_streak: # this is done after both branch results
                best_streak = current_streak 
                best_char = current_char

        return best_char + str(best_streak)

s = Solution()

print(s.longestRun("bbacccdbbab"))  # expected: c3
print(s.longestRun("aabbcc"))       # expected: c2
print(s.longestRun("zzzz"))         # expected: z4
print(s.longestRun("abc"))          # expected: c1
print(s.longestRun("aaabbbaaa"))    # expected: a3
print(s.longestRun("x"))            # expected: x1