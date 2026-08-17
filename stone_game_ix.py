from collections import Counter

# credit: lee215
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(x % 3 for x in stones)

        # when cnt[0] is even, 
        # the game is equivalent to having no cnt[0]=0

        if cnt[0]%2 == 0:
            # Alice will win if both cnt[1] & cnt[2] > 0, she will choose the one with lower frequency
            # if cnt[1] or cnt[2] = 0 then whoever goes first loses or it's a tie (still Alice's loss)
            # i.e. only cnt[1] > 0, 1 -> 2 -> 0; only cnt[2] > 0, 2 -> 1 -> 0;
            return cnt[1] > 0 and cnt[2] > 0
        
        else:
            # cnt[0] gives opportunity to flip to winning side
            # choosing two 2s has same effect as choosing 1
            # choosing two 1s has same effect as choosing 2
            return abs(cnt[1]-cnt[2]) > 2
