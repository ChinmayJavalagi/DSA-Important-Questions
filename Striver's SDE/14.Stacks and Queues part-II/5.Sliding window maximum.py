from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pq = deque() #will hold index
        l = r = 0
        res = []


        while r<len(nums):

            #pop smaller elements in pq
            while pq and nums[r]>nums[pq[-1]]:
                pq.pop()

            #append present max element
            pq.append(r)

            #remove left value from the window
            if l>pq[0]:
                pq.popleft()
            
            #update the res only if r is minium k
            if r+1>=k:
                res.append(nums[pq[0]])
                l+=1
            r+=1
        return res
