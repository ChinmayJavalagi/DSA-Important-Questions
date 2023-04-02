'''Keep two lists to store i and j wherever we get a 0, 
then traverse the matrix and check if either of i or j is present in first list or second, 
if present set matrix[i][j] = 0'''

# TC - O(N*M + N*M)
# SC - O(N)

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        arr = []
        arr1 = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    arr.append(i)
                    arr1.append(j)
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j in arr1 or i in arr:
                    matrix[i][j] = 0


        return matrix
