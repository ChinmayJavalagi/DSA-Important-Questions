#Binary exponentiation method
#pow(x, n)
"""
1. Inititalise ans = 1.
2. Check for negative exponent.
3. if n is even, x = x*x and n = n//2
    Ex: 2**10 --> (2*2)**5

4. if n is odd, ans = ans*x and n = n-1
    Ex: 4**5 --> 4*(4**4)
"""

class Solution(object):
    def myPow(self, x, n):
        ans = 1
        m = n
        if m<0:
            m = -1*m
        while m:
            if m%2:
                ans = ans*x
                m = m - 1
            else:
                x = x*x
                m = m//2
        if n<0:
            ans = 1.0/ans
        return ans
