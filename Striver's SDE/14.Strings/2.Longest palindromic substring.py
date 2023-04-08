#DP solution


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        reslen = 0
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                r+=1
                l-=1
            
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l+1>reslen:
                    reslen = r-l+1
                    res = s[l:r+1]
                r+=1
                l-=1
        
        return res
