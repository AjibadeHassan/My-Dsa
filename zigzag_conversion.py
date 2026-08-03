class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        mat = [[] for _ in range(numRows)]
        i = 0
        n = len(s)

        while i < n:
            for down in range(numRows):
                if i < n:
                    mat[down].append(s[i])
                    i += 1
            for up in range(numRows - 2, 0, -1):
                if i < n:
                    mat[up].append(s[i])
                    i += 1

        ans = ""
        for row in mat:
            ans += ''.join(row)
        return ans
