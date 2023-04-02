#Rotate the matrix 90 degrees clockwise

""" 
1. Transpose the matrix (Swap i, j to j, i and j, i to i, j)
2. Take the mirror image (matrix.reverse)
"""

#TC - O(N*N)
#SC - O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        
