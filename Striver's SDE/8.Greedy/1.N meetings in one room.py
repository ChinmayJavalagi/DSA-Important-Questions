#Think Greedy be Greedy
"""
1. Add both 'start' and 'end' to a data structure and sort it based on 'end' values.
2. Set a limit i.e. the end of first meeting so that we can start comparing.
3. Iterate and compare if the present start value is greater than the limit.
      if yes, cnt++ and set limit to the end value of that meeting.
"""
#TC - O(n) +O(n log n) + O(n) ~O(n log n)
#SC - O(n)

Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        meet = []
        for i in range(n):
            meet.append([end[i], start[i]])
        meet.sort()
        
        res = 1
        limit = meet[0][0]
        for i in range(1,n):
            if meet[i][1] > limit:
                res+=1
                limit = meet[i][0]
        return res
        
