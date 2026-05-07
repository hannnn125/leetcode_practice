from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n=len(senate)
        r_que=deque()
        d_que=deque()

        for i,s in enumerate(senate):
            if s =='R':
                r_que.append(i)
            else:
                d_que.append(i)
        while r_que and d_que: 
            r_idx=r_que.popleft()
            d_idx=d_que.popleft()
            if r_idx<d_idx:
                r_que.append(r_idx+n)
            else:
                d_que.append(d_idx+n)
        return "Radiant" if r_que else "Dire" 