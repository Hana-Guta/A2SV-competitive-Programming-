from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        for row in range(N):
            for col in range(row, N):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in matrix:
            start = 0
            end = N - 1
            while start < end:
                row[start], row[end] = row[end], row[start]
                start += 1
                end -= 1
