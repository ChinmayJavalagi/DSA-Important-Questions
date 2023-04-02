"""
Using Three pointer approach.

1.Initialise low = 0, mid = 0, high = len(nums)-1
2.Iterate through the array, 
      if mid element is 0 swap mid and low and increment both.
      if mid element is 1 increment mid.
      if mid element is 2 swap mid and high, decrement high.
"""

# TC - O(N)
# SC - O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid<=high:
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid+=1
                low+=1
            elif nums[mid] == 1:
                mid+=1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1   
