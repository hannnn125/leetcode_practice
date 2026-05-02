from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.request = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.request.append(t)
        while self.request[0]<t-3000:
            self.request.pop(0)
        return len(self.request)


"""
최근 3000ms 이내에 들어온 요청의 개수를 반환하는 클래스
request 리스트를 사용하여 요청을 저장
ping 함수에서 t를 받아서 request 리스트에 추가
request[0]가 이상일때까지 t-3000ms 제거 
request 리스트의 길이를 반환
"""


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)