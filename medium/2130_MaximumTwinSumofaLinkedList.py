# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        
        중간 지점을 찾아서 접은 다음(리버스) 더해가면서 maxsum 확인
        """

        one=head
        two=head
        while two and two.next:
            one=one.next
            two=two.next.next 
        
        #나머지 반 리버스
        prev = None
        curr = one
        while curr: 
            next_node = curr.next 
            curr.next = prev
            prev=curr
            curr= next_node

        #최대합 구하기 
        
        while prev:
            max_sum = max(max_sum, head.val+prev.val)
            head = head.next
            prev=prev.next
        return max_sum


        