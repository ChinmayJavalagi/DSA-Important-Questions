#m -> len(nums1) , n-> len(nums2)
#TC - O(n+m) 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return nums1 
        if m == 0:
            nums1[:] = nums2
        else:
            i,j = 0,0
            while j<n and i<n+m-1:
                if nums1[i]>nums2[j]:
                    nums1.insert(i,nums2[j])
                    j+=1
                    i+=1
                else:
                    i+=1
            nums1[m+j:] = nums2[j:] 
