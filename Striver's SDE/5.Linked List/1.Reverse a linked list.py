#TC - O(n)
class Solution(object):
    def reverseList(self, head):
        cur = head
        prev = None
        while cur !=None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
