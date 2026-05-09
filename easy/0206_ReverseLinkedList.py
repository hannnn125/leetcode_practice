# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #e.g., 1->2->3
        prev = None 
        current = head 
        while current: 
            next_node = current.next #우선 다음노드를 저장해두고  next_node = 2
            current.next=prev #다음노드를 prev로 잡음 화살표를 돌림 1->None
            prev=current #prev를 다음칸로 이동 prev=1
            current=next_node #저장해뒀던 다음노드를 현재값으로 current=2

            '''
            1
            next_node=2
            1->None
            prev=1
            current=2

            2차
            next_node=3
            2->1 
            prev=2
            current=3
            
            3차 
            next_node=None
            3->2
            prev=3
            current=None
            '''
            
        return prev 