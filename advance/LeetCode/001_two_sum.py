"""
@Author: genejiang
@Date: 2019-10-23 13:57:04
@LastEditTime: 2019-10-23 14:00:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath:
"""


class Solution:
    def two_sum(self, nums, target):
        """
        :nums: one list with integer
        :target: the target number
        """
        hash_table = {}
        for index, value in enumerate(nums):
            if target - value in hash_table:
                return (hash_table[target-value], index)
            hash_table[value] = index


solution = Solution()
print(solution.two_sum([2, 7, 11, 13, 14], 9))


