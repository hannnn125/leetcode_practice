class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i <len(nums): 
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
            i+=1
        return -1 

'''
1차 시도: 실패
피봇 인덱스를 i 로 잡고 i왼쪽 합이 i오른쪽 합과 같은 경우 인덱스, i가 len(nums)를 넘어가는 경우 -1 리턴
len(nums)-1 로 마지막 값이 피봇인 경우 고려 안함..
2차 시도: 성공
'''