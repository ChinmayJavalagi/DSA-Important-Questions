#Extended Moore's voting algorithm
"""
There will be atmost 2 majority elements which will be repeated more than n/3 times.
So we take 2 variable to hold two maj eles and do the same as we did for Majority Element I question.
"""


class Solution(object):
    def majorityElement(self, nums):        
        num1,num2,cnt1,cnt2 = -1,-1,0,0
        for num in nums:
            if num1 == num:
                cnt1+=1
            elif num2 == num:
                cnt2+=1
            elif cnt1 == 0:
                num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                cnt2 = 1
                num2 = num
            else:
                cnt1-=1
                cnt2-=1
        
        arr = []
        if nums.count(num1)>len(nums)//3:
            arr.append(num1)
        if nums.count(num2)>len(nums)//3:
            arr.append(num2)
        return set(arr)
