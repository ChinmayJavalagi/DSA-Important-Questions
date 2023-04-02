"""
1. Sort the array
2. Create a new array, Iterate, check if end of interval is less than start of next interval
      if yes, then we shouldn't merge
      if no, we should merge, so we will take the max of end of present and next interval. 

"""
#TC - O(nlogn)
#SC - O(n)

from typing import List
def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort()
    merged = []

    for i in range(len(intervals)):
        if not merged or merged[-1][1] < intervals[i][0]:
            merged.append(intervals[i])
        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])


    return merged
