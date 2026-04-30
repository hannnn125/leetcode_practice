class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if sum(nums)<k:
            return 0
        pair = {}
        operation = 0
        for i in nums: 
            target = k-i 
            if pair.get(target,0)>0:
                operation +=1
                pair[target] -= 1
            else: 
                pair[i]=pair.get(i,0)+1
        return operation 

'''
창고하나 만들어두고 
nums 돌면서 창고에 짝이 있으면 가져다 쓰고 opr 1증가 없으면 창고에 넣어둠 
'''   



        