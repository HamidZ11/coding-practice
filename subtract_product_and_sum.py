class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        strnum = str(n)
        digitsum = 0 
        digitproduct = 1

        for i in strnum:
            digit = int(i)
            digitsum = digitsum + digit
            digitproduct = digitproduct * digit

        return digitproduct - digitsum


s = Solution()

print(s.subtractProductAndSum(234))      # expected: 15
print(s.subtractProductAndSum(123456))   # expected: 699
print(s.subtractProductAndSum(4421))     # expected: 21
print(s.subtractProductAndSum(101))      # expected: -2
print(s.subtractProductAndSum(5))        # expected: 0      