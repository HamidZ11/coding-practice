def longestBalanced(nums: list[int]) -> int:

    # you cannot use two pointers because you do not know what the next number is

    # the key is repeated-balance, track one number called balance, 
    # 1 -> blance += 1 , 0 -> balance -= 1

    balance = 0
    bal_dict = {0: -1}
    current_len = 0
    max_len = 0

    for index, num in enumerate(nums):
        if num == 1:
            balance += 1
        else: 
            balance -= 1

        if balance in bal_dict:
            current_len = index - bal_dict[balance]
            max_len = max(max_len, current_len)
        else:
            bal_dict[balance] = index

    return max_len















## The below code does not work when the subarray does not start at index 0 

#   max_len = 0 
#   current_len = 0 
#   one_count = 0
#    zero_count = 0 
#
#    for num in nums: 
#        if num == 0:
#            zero_count += 1
#        else:
#            one_count += 1
#
#        if zero_count == one_count:
#            current_len = one_count *  2
#            max_len = max(max_len, current_len)

#    return max_len



print(longestBalanced([0, 1]))                    # expected: 2
print(longestBalanced([0, 1, 0]))                 # expected: 2
print(longestBalanced([0, 0, 1, 0, 1, 1]))       # expected: 6
print(longestBalanced([1, 1, 1, 0, 0]))          # expected: 4
print(longestBalanced([0, 0, 0]))                 # expected: 0
print(longestBalanced([1, 0, 1, 1, 0, 0]))       # expected: 6
print(longestBalanced([1]))                       # expected: 0