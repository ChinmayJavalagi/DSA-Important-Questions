#Method 1
''' 1.Build a frequency dictionary - invert the sign of the frequency (-ve frequency serves as priority key for the heap later)
    2.Push all (item, -ve freq) pairs into heap
    3.Pop k items from heap and append to a result list
    4.return list
'''
# TC - O(N*logN)
# SC - O(N)

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        pq = []
        li = []
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d.keys():
            heapq.heappush(pq,[-d[i],i])
        print(pq)
        for i in range(k):
            li.append(heapq.heappop(pq)[1])
        return li


#Optimised
'''
    1.Build a frequency dictionary (freq is positive)
    2.Build a heap
    3.Make sure heap conatins k items at maximum by popping out the items with least frequency as you push to heap
    4.The time complexity of adding an element in a heap is O(log(k)) and we do it N times that means O(Nlog(k)) time complexity for this step.
    5.Heap now contains k items (the desired output basically)
    6.Pop and append to the output list - O(klog(k))
    7.return list
'''
# Optimised
# TC - O(N*logK)
# SC - O(N)

import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        pq = []
        d = {}
        for num in (nums):
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for i in d.keys():
            if len(pq) == k:
                heapq.heappushpop(pq, (d[i], i))
            else:
                heapq.heappush(pq, (d[i], i))
                
        res = []
        while k>0:
            res.append(heapq.heappop(pq)[1])
            k-=1
        return res
