"""
{
	"id": 141,
	"name": "Linked List Cycle",
	"difficulty": "easy",
	"link": "https://leetcode.com/problems/linked-list-cycle/description/",
	"tags": ["two pointers"]
}
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        p1,p2 = head, head.next
        if not p2:
            return False
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
            if p1 and p2:
                p2 = p2.next
                if not p2:
                    return False
            else:
                return False
        return True
            