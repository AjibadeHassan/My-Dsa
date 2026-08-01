from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * n

        indexSum = defaultdict(int)
        indexFreq = defaultdict(int)
        
        #left to right
        for i in range(n):
            freq = indexFreq[nums[i]]
            sum_ = indexSum[nums[i]]

            arr[i] += freq * i - sum_

            indexFreq[nums[i]] += 1
            indexSum[nums[i]] += i

        indexFreq.clear()
        indexSum.clear()

        #right to left
        for i in range(n - 1, -1, -1):
            freq = indexFreq[nums[i]]
            sum_ = indexSum[nums[i]]

            arr[i] += sum_ - freq * i

            indexFreq[nums[i]] += 1
            indexSum[nums[i]] += i

        return arr
