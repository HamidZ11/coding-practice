def longestBalancedSegment(nums: list[int]) -> int:

        balance = 0
        max_length = 0

        first_seen = {0: -1}

        for index, num in enumerate(nums):

            if num == 0:
                  balance -= 1
            else:
                  balance += 1

            if balance in first_seen:
                 length = index - first_seen[balance]
                 if length > max_length:
                       max_length = length
            else:
                    first_seen[balance] = index

        return max_length
                  
              
        




print(longestBalancedSegment([0, 1]))                    # expected: 2
print(longestBalancedSegment([0, 1, 0]))                 # expected: 2
print(longestBalancedSegment([0, 0, 1, 0, 1, 1, 0]))    # expected: 6
print(longestBalancedSegment([0, 0, 0, 1, 1, 1]))       # expected: 6
print(longestBalancedSegment([1, 1, 1, 0, 0]))          # expected: 4
print(longestBalancedSegment([0, 0, 0]))                # expected: 0
print(longestBalancedSegment([1, 1, 1]))                # expected: 0
print(longestBalancedSegment([0, 1, 1, 0, 1, 0]))       # expected: 6
print(longestBalancedSegment([1]))                      # expected: 0