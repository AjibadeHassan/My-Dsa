from bisect import bisect_left
from sortedcontainers import SortedList

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution(object):
    def getResults(self, queries):
        MAXX = 50000

        obstacles = SortedList([0, MAXX])

        gaps = []
        for q in queries:
            if q[0] == 1:
                gaps.append(q[1])

        for x in gaps:
            obstacles.add(x)

        bit = Fenwick(MAXX + 2)

        for i in range(1, len(obstacles)):
            bit.update(obstacles[i], obstacles[i] - obstacles[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]

                idx = obstacles.bisect_right(x) - 1
                prev_obs = obstacles[idx]

                best = bit.query(x)
                best = max(best, x - prev_obs)

                ans.append(best >= sz)

            else:
                x = q[1]

                idx = obstacles.bisect_left(x)

                left = obstacles[idx - 1]
                right = obstacles[idx + 1]

                obstacles.remove(x)

                bit.update(right, right - left)

        return ans[::-1]
