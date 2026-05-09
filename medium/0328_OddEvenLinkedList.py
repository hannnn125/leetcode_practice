# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        홀수 포인터,짝수 포인터 만들고 각각 이어나간다음 홀수 뒤에 짝수 Head 붙여서 연결
        """
        if not head or not head.next:
            return head

        odd_node = head 
        even_node = head.next
        even_head = head.next

        while even_node and even_node.next: 
            odd_node.next = odd_node.next.next
            odd_node = odd_node.next

            even_node.next = even_node.next.next
            even_node = even_node.next
        odd_node.next=even_head
        return head
        