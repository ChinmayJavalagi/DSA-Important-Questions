#Sliding window 
#Kadane's Algo
"""
1. Initialize max_sum = -inf and temp_sum = 0
2. Iterate through the array, add the val to temp_sum. 
3. If temp_sum is negative reset it to 0 (becoz taking -ve values furthur isn't useful).
    elif temp_sum is greater than max_sum assign max_sum ---> temp_sum.  
"""
# TC - O(N)
# SC - O(1)


class Solution(object):
    def maxSubArray(self, a):
      
        ts,ms = 0, float('-inf')
        for num in a:
            ts+=num
            ms = max(ms, ts)
            ts = max(0,ts)
        return ms
