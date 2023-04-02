#Moore's Voting Algorithm

"""
1. Inititalise ans = arr[0]
2. keep a count variable, count++ if the same number is found else count--.
3. whenever the count becomes 0, reassign the ans to arr[i+1] and count = 1.
4. At the end of the traversal we get the ans as majority element if there always exist one, else arr.count(ans) should be greater than n//2.
"""
#Time Complexity: O(N) + O(N)
#Space Complexity: O(1)

class Solution(object):
    def majorityElement(self, nums):
        cnt, res = 0,0
        for num in nums:
            if cnt == 0:
                res = num
            cnt+=(1 if num == res else -1)
        return res
