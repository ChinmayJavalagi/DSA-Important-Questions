"""
1. Search in which row the value might be present
2. Apply binary search in that row
"""
#Time complexity: O(log(m*n))
#Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if target <= matrix[i][-1]:
                break
        l,h = 0, c-1
        while l<=h:
            m = (l+h)//2
            if matrix[i][m] == target:
                return True
            elif matrix[i][m] <= target:
                l = m+1
            else:
                h = m-1
        return False

    
#approach 2
'''
Streach the matrix by considering it as a linear array, if 3x4 matrix, we can say it as a linear array of length 12(3x4).
Do binary search
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        low,high = 0,((m*n)-1)
        while low<=high:
            middle = (low+high)//2  
            if matrix[middle//n][middle%n]>target:
                high = middle-1
            elif matrix[middle//n][middle%n]<target:
                low = middle+1
            else:
                return True
        return False
