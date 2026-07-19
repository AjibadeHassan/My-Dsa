# GCD(a, b) = GCD(b, a % b)
class Solution(object):
    def findGCD(self, nums):
        mini = min(nums)
        maxi = max(nums)

        while maxi != 0:
            mini, maxi = maxi, mini % maxi

        return mini
