# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values_of_linked=[]
        node=head
        while 1:
            values_of_linked.append(node.val)
            if node.next==None:
                break
            node=node.next
        
        for i,j in zip(values_of_linked,values_of_linked[::-1]):
            if   i!=j:
                return 0
        return 1
            
        
        
        
        