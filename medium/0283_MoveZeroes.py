class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonzero=[x for x in nums if x !=0]
        nums[:] = nonzero+[0]*(len(nums)-len(nonzero))
        return nums

"""
1차 시도: 성공
리스트 내 0개수 확인 후 num 돌면서 0 모두 remove해줌-> nums에 nums+0개수만큼 넣음

그러나 .remove(0)는 호출될 때마다 리스트의 처음부터 끝까지 0이 어디 있는지 찾고, 0을 지운 뒤에 뒤에 있는 숫자들을 한 칸씩 앞으로 당기는 작업을 수행 해서 느림 Beats 5%

2차 시도 for 문 돌면서 nonzero 만 리스트에 남기고 
nonzero 리스트에 [0]*(nums 전체 개수 - nonzero 개수 = zero 개수 추가 ) Beats 79%
"""      
        