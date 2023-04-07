'''Intution - we usually merge by having pointers.so that in the heap, elements from all the array must be present at once.
    1. first add all the first element of k arrays to min heap.
    2. Pop the min ele and add it to ans
    3. Then add the next ele of that particular array to heap.So that we have elements from all the array.
    4. Pop until heap becomes empty.
'''

import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        res = []
        pq = []
        for i in range(K):
            heapq.heappush(pq, (arr[i][0], i, 0))
        
        while pq:
            val, arr_ind, val_ind = heapq.heappop(pq)
            res.append(val)
            if val_ind+1<K:
                heapq.heappush(pq, (arr[arr_ind][val_ind+1], arr_ind, val_ind+1))
            
        return res
