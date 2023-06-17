#bruteforce
'''Keep two lists to store i and j wherever we get a 0, 
then traverse the matrix and check if either of i or j is present in first list or second, 
if present set matrix[i][j] = 0'''


#optimal
# TC - O(N*M + N*M)
# SC - O(1)
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        col = 1
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i == 0:
                        col = 0
                    else:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
        
        print(matrix)
        for i in range(1,r):
            if matrix[i][0] == 0:
                for j in range(1,c):
                    matrix[i][j] = 0
        print(matrix)

        for j in range(c):
            if matrix[0][j] == 0:
                for i in range(1,r):
                    matrix[i][j] = 0
        print(matrix)

        if col == 0:
            for j in range(c):
                matrix[0][j] = 0
