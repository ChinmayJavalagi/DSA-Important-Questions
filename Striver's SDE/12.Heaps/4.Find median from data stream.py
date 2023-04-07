''' 1. We will create two heaps small heap(max heap) and large heap(min heap).
    2. Whenever median is required to find ans will be (max of small heap + min of large heap) / 2 for even and max(small) or min(large) for odd.
    3. We add a new element to small heap always.And if the small[0] > large[0] that means the ele should be placed in large heap bcoz its not smaller.
    4. And we always have to make sure that diff of len of both heap should be atmost 1.
    5. If len(small)>len(large)+1 then pop  the max of small and push to large heap.
    6. If len(large)>len(small)+1 then pop the min of large and push to small heap.
    7. Find Median.
'''

import heapq
class MedianFinder(object):

    def __init__(self):
        #two heaps, small and large 
                  #minheap and maxheap
        self.small, self.large = [], []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.small, -1*num)

        #make sure evey element in small is <= every element in large
        if (self.small and self.large and (-1*self.small[0] and self.large[0])):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]        
        return (-1*self.small[0] + self.large[0])/2.0
