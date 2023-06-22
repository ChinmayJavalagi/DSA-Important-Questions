class Solution(object):
    def generate(self, n):
        li = [[1]*(i+1) for i in range(n)]
        
        for i in range(2,n):
            for j in range(1,i):
                li[i][j]=li[i-1][j-1]+li[i-1][j]
                
        return li
