class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        unseen = [[1]*n for _ in range(m)]
        res = m * n

        for i, j in walls + guards:
            unseen[i][j] = 0
            res -= 1

        for i, j in guards:
            for k in range(j-1, -1, -1):
                if unseen[i][k] == 1:
                    unseen[i][k] = -1
                    res -= 1
                elif unseen[i][k] == 0:
                    break

            for k in range(j+1, n):
                if unseen[i][k] == 1:
                    unseen[i][k] = -1
                    res -= 1
                elif unseen[i][k] == 0:
                    break

            for k in range(i-1, -1, -1):
                if unseen[k][j] == 1:
                    unseen[k][j] = -1
                    res -= 1
                elif unseen[k][j] == 0:
                    break

            for k in range(i+1, m):
                if unseen[k][j] == 1:
                    unseen[k][j] = -1
                    res -= 1
                elif unseen[k][j] == 0:
                    break

        return res
