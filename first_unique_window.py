class Solution:
    def firstUniqueWindow(self, s: str, k: int) -> int:

        for i in range(len(s) - k + 1): # this is the only valid range for a window of length k to appear

            window = s[i:i + k] # window is from the index of s from i to i+k
        
            char_set = set() 
            is_unique = True 
            for char in window: 
                if char in char_set: # you just need to check the window for duplicate characters, not the whole string
                    is_unique = False
                else:
                    char_set.add(char)
            

            if is_unique:
                return i

        return -1   
            
            


s = Solution()

print(s.firstUniqueWindow("abcaefg", 4))   # expected: 1
print(s.firstUniqueWindow("aaaaa", 2))     # expected: -1
print(s.firstUniqueWindow("xyz", 3))       # expected: 0
print(s.firstUniqueWindow("abcabcbb", 3))  # expected: 0
print(s.firstUniqueWindow("aabbcde", 3))   # expected: 3
print(s.firstUniqueWindow("abccdef", 3))   # expected: 0
print(s.firstUniqueWindow("zzabc", 2))     # expected: 1
print(s.firstUniqueWindow("abcde", 5))     # expected: 0