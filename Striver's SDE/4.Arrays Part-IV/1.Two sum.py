#Method 1

#TC - O(n)
#SC - O(n)
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        res = []
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                res.append(i)
                res.append(d[target-nums[i]])
                return res
            d[nums[i]] = i
        return res
        
        
#Method 2 (two pointers, binary search)

#TC - O(nlogn)
#SC - O(1)

"""
1. Sort the array
2. Initialise left = 0 and right = len(arr)-1
3. run a loop until left becomes greater than or equal to right
4. Check if arr[right]+arr[left] == sum
      if yes append it in the data structure,
      else if >sum, right--
      else if <sum, left++
"""
