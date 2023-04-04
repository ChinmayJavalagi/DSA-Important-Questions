"""
1. Push all the elements into min or max heap.
2. Pop all the elements till k-1
3. Return pq[0]
"""


# TC - O(N*logN) +  O(K*logN)
#          |           |
#   building max   Extracting max/min
#        heap           ele


def kthLargest(self,a,n,k):
        pq = []
        for i in range(n):
            heapq.heappush(pq,-a[i])
        for i in range(k-1):
            heapq.heappop(pq)
        return -pq[0]
      
 
class Solution:
    #Function to find the kth smallest element in the array.
    def kthSmallest(self,a,n,k):
        heapq.heapify(a)
        for i in range(k-1):
            heapq.heappop(a)
        return a[0]
