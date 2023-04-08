#Naive or bruteforce
"""
S = abceabcdabceabcdd
P = abcdd

We can use the concept of sliding window.
We start with i = 0 till n-m+1 and in while loop j=0 to j = m-1 (to check every char in pattern if it matches with string within that window)
1. We run a loop for every letter in s and in another looop we check if s[i+j] == p[j].
2. if yes then return True else after the loop, return False
"""

#TC - O((n-m+1)*m)
#SC - O(1)
class Solution:
    def search(self,p,s):
        m = len(p)
        n = len(s)
        
        for i in range(n-m+1):
            j = 0
            while j<m:
                if p[j] != s[i+j]:
                    break
                j+=1
            
            if j == m:
                return True
        return False
      
#Naive or bruteforce for distinct pattern matching
"""
We already know that the pattern has distinct elements, so we make use of this and modify the above Naive approach.

txt = "ABCEABFABCD"
pat = "ABCD"

1. When we start a loop from i=0 inside a for loop we check if all the elements in the pat are matching with elements in txt of size m.
2. While matching, if we find an element which doesn't match we skip the next iterations of the characters in txt and jump to i +=j.

In the above example, txt[0] == pat[0] till txt[2] == pat[2] but when we come to the 3rd index we see that E isn't matching with D so we skip the window to 3rd index and start cheching from there(i+=j), in contrast to what we did in the abouve approach(incrementing i by 1).

Intuition: If we already know that A is matching with A and B is matching with B and so on ofcourse if we slide by i+1 we can say that A(in pat) doesn't match with B(in txt). 
"""

#TC - O(n-m+1)
def distpatsearch(txt, pat) :
    m = len(pat)
    n = len(txt)
    i = 0
    while i <= (n-m) :
        for j in range(m) :
            if pat[j] != txt[i + j] :
                break
            j += 1
        if j == m :
            print(i, end = " ")
            i += m
        if j == 0 :
            i += 1 
        else :
            i += j 
   


#Rabin-Karp Algorithm
"""
1. Initially calculate the hash value of the pattern.
2. Start iterating from the starting of the string:
        ->Calculate the hash value of the current substring having length m.
        ->If the hash value of the current substring and the pattern are same check if the substring is same as the pattern(like naive).
        ->If they are same, store the starting index as a valid answer (here we are just returning true). Otherwise, continue for the next substrings.
3.Return the starting indices as the required answer(here true or false).
"""

"""
***Spurious Hits***
When the hash value of the pattern matches with the hash value of 
a window of the text but the window is not the actual pattern then it is called a spurious hit.

Spurious hit increases the time complexity of the algorithm. In order to minimize spurious hit,
we use modulus. It greatly reduces the spurious hit.
"""

#TC - O((n-m+1)*m) ->Worst case (all spurious hits, "AAAAA", "AAA")
   #- O(m + n) -> Average/Best case      

class Solution:
    def search(self,p,s):
        # d is the number of characters in the input alphabet
        d = 256
        
        def rksearch(pat,txt,q):
            #q -> A prime number
            m = len(pat)
            n = len(txt)
            h = 1
            p = 0     # hash value for pattern
            t = 0     # hash value for txt
            
            # The value of h would be "pow(d, M-1)%q"
            for i in range(1,m):
                h = (h*d)%q
            
            # Calculate the hash value of pattern and first window of text
            for i in range(m):
                p = (p*d + ord(pat[i]))%q
                t = (t*d + ord(txt[i]))%q
            
            # Slide the pattern over text one by one
            for i in range(n-m+1):
                
                ''' Check the hash values of current window of text and
                pattern if the hash values match then only check 
                for characters one by one.'''

                if p == t:
                    #Check for spurious hits.
                    for j in range(m):
                        if pat[j]!=txt[i+j]:
                            break
                    else:
                        return True
                    
                # Calculate hash value for next window of text:
                            #->Remove leading digit, add trailing digit
                if i<n-m:
                    t = (d*(t-ord(txt[i])*h) + (ord(txt[i+m])))%q
                    
                    # We might get negative values of t, converting it to positive
                    if t<0:
                        t+=q
                        
        return rksearch(p, s, 1009)
    
    
    
    
