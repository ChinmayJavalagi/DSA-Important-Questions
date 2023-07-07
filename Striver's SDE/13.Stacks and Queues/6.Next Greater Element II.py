#TC - O(n+m)

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stack = [nums[-1]]
        nge = [-1]*(2*n)
        # nums = [1,2,1,1,2,1]
        for i in range(2*n-2, -1, -1):
            while stack and stack[-1]<=nums[i%n]:
                stack.pop()
            
            if not stack:
                stack.append(nums[i%n])
                continue
            nge[i] = stack[-1]
            stack.append(nums[i%n])
            
        return nge[:n]
