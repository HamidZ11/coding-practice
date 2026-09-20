class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strnum = str(n)
        listnum = []
        product_num = 1

        for i in strnum:
            listnum.append(int(i))

        for i in listnum:
            product_num = product_num * int(i)

        num_sum = sum(listnum)

        return product_num - num_sum



s = Solution()

print(s.subtractProductAndSum(234))      # expected: 15
print(s.subtractProductAndSum(123456))   # expected: 699
print(s.subtractProductAndSum(4421))     # expected: 21
print(s.subtractProductAndSum(101))      # expected: -2
print(s.subtractProductAndSum(5))        # expected: 0      