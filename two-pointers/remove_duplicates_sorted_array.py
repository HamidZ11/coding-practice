class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        left = 0
        # nums[left] is our first unique value

        for right in range(1, len(nums)):
            if nums[right] > nums[right - 1]: #if your number is greater than the previous number it absolutely must be a new number (unique value)

                # then we want to add this value to where the left pointer is currently pointing
                left += 1
                nums[left] = nums[right]

            # now, what about an else case
            # well for this problem you ONLY NEED TO OVERWRITE THE FRONT OF THE ARRAY WITH UNIQE VALUES
        
        return left + 1 #left moves up one index each time we discover a duplicate




nums = [1, 1, 2]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])  
# expected: 2 [1, 2]


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])
# expected: 5 [0, 1, 2, 3, 4]


nums = [1, 1, 1, 1]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])
# expected: 1 [1]


nums = [1, 2, 3, 4]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])
# expected: 4 [1, 2, 3, 4]


nums = [0]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])
# expected: 1 [0]


nums = [-3, -3, -2, -1, -1, 0, 0, 0, 4]
k = Solution().removeDuplicates(nums)
print(k, nums[:k])
# expected: 5 [-3, -2, -1, 0, 4]