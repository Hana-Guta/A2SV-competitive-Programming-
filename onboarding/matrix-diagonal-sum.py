class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        n = len(mat)

        for i in range(n):
            first = mat[i][i]
            sec = mat[i][n - i - 1]

            res += (first + sec )
        return (res - (mat[n//2][n//2] if n % 2 else 0))
        