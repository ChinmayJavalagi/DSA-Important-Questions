#using logarithm
import math
class Solution:
    def digitsInFactorial(self,N):
        # code here
        res = 0
        for i in range(2, N+1):
            res+=math.log10(i)
        return math.floor(res)+1


#using Stirling's approximation
import math
class Solution:
    def digitsInFactorial(self, n):
        
        if n < 0:
            return 0

        if n <= 1:
            return 1
        sa = (n * math.log10(n / math.e) + math.log10(2 * math.pi * n) / 2.0)
        return math.ceil(sa)
