class Solution(object):

    def two_sum(self, nums, target):
        n = len(nums)
        for x in range(n):
            for y in range(x+1, n):
                if nums[y] == target - nums[x]:
                    return x, y


if __name__ == '__main__':
    sol = Solution()
    print(sol.two_sum([1, 3, 5, 10, 2], 15))
    print(sol.two_sum([0, 0, 0], 0))
