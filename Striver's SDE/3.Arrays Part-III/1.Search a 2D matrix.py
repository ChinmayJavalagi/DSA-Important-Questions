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
