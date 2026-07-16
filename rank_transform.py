class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = []
        num_rank = {}

        for num in arr:
            if num not in num_rank:
                unique_arr.append(num)
                num_rank[num] = 0

        unique_arr.sort()

        for i, num in enumerate(unique_arr):
            num_rank[num] = i + 1

        return [num_rank[num] for num in arr]
