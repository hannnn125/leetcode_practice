# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        중간인덱스(n/2) 삭제
        배수 2칸씩 이동해서 몇 배수에서 끝나는지 알면됨 
        2배수가 끝에 도달했을때 그 위치에 중간값이 있도록 동일 iter에 1/2씩 이동하는 Pointer 

        """
        if not head or not head.next:
            return None

        one_node = head
        two_node = head
        while two_node or two_node.next:
            prev=one_node
            one_node=one_node.next
            two_node=two_node.next.next
        prev.next = one_node.next
        return head

