""" The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
    
    Input: nums = [1,2,3]         Input: nums = [3,2,1]
    Output: [1,3,2]               Output: [1,2,3]
    
    1.Traverse from back, look for num smaller than previous num (nums[i]<nums[i+1]), call it as "First".
    2.Traverse from back till first, look for num just greater than "First", call it as "Second".
    3.Swap "First" and "Second".
    4.Reverse the list from First+1.
    
"""

# TC - O(N)
# SC - O(1)

class Solution(object):
    def nextPermutation(self, nums):

        k = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                k = i
                break
        if k==-1:
            nums.reverse()
        else:

            for j in range(len(nums)-1,i-1,-1):
                if nums[j]>nums[i]:
                    break
        
            nums[i], nums[j] = nums[j], nums[i]

            nums[i+1:] = nums[i+1:][::-1]
