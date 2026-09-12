class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        max_score = 0 
        num_set = set(nums) # easy lookup

        for num in nums:
            if num - 1 not in num_set: # crucial check, it checks if this is the start of the array
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1

                max_score = max(max_score, current_length)

        return max_score
       

s = Solution()

print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  
# expected: 4

print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  
# expected: 9

print(s.longestConsecutive([10, 30, 20]))  
# expected: 1

print(s.longestConsecutive([1, 2, 3, 4, 5]))  
# expected: 5

print(s.longestConsecutive([5, 4, 3, 2, 1]))  
# expected: 5

print(s.longestConsecutive([1, 2, 2, 3]))  
# expected: 3

print(s.longestConsecutive([]))  
# expected: 0