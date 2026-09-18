def longestUniqueSubstring(s: str) -> int:

    left = 0 
    char_set = set()
    max_length = 0
    
    for right in range(len(s)):
        if s[right] not in char_set:
            char_set.add(s[right])
            current_length = right - left + 1


print(longestUniqueSubstring("abcabcbb"))  # expected: 3
print(longestUniqueSubstring("bbbbb"))     # expected: 1
print(longestUniqueSubstring("pwwkew"))    # expected: 3
print(longestUniqueSubstring(""))          # expected: 0
print(longestUniqueSubstring("abcdef"))    # expected: 6
print(longestUniqueSubstring("abba"))      # expected: 2
print(longestUniqueSubstring("dvdf"))      # expected: 3
print(longestUniqueSubstring("aab"))       # expected: 2
print(longestUniqueSubstring("tmmzuxt"))   # expected: 5