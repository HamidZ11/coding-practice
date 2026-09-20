def lengthOfLongestSubstring(s: str) -> int:

    left = 0 
    char_set = set()
    max_length = 0

    for right in range(len(s)):

        while s[right] in char_set: # if we come across a duplicate value
            char_set.remove(s[left]) # remove the left most value from our set 
            left += 1 # move left one space forward 
            
        char_set.add(s[right]) # add it to our set 
        
        current_length = right - left + 1
        max_length = max(max_length, current_length)


    return max_length



print(lengthOfLongestSubstring("abcabcbb"))  # expected: 3
print(lengthOfLongestSubstring("bbbbb"))     # expected: 1
print(lengthOfLongestSubstring("pwwkew"))    # expected: 3
print(lengthOfLongestSubstring(""))          # expected: 0
print(lengthOfLongestSubstring("a"))         # expected: 1
print(lengthOfLongestSubstring("dvdf"))      # expected: 3
print(lengthOfLongestSubstring("tmmzuxt"))   # expected: 5
print(lengthOfLongestSubstring("abba"))      # expected: 2