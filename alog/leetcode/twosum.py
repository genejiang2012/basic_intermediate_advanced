#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (41.43%)
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#
import pdb
pdb.set_trace()



class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            left = nums[i+1:]
            for j in range(len(left)):
                if (nums[i]+left[j]) == target:
                    return i, j+i+1


class SolutionSecond:
    def twoSum(self, nums, target):
        k = 0
        for i in nums:
            k += 1
            if target - i in nums[k:]:
                return (k-1, nums[k:].index(target-i) + k)


class SolutionThird:
    def two_sum(self, nums, target):
        """
        :nums: one list with integer
        :target: the target number
        """
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return (hash_table[target-num], i)
            hash_table[num] = i


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 26))

    sol2 = SolutionSecond()
    print(sol2.twoSum([2, 7, 11, 15], 18))

    sol3 = SolutionThird()
    print(sol3.two_sum([2, 7, 11, 15], 26))
