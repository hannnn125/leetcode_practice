'''
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, 
return false.
'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first=max(nums)
        second=max(nums)
        for num in nums: 
            if num <= first: 
                first = num
            elif num <= second:
                second = num
            else: #num 이 first, second 보다 커서 넘어옴
                return True
        return False

'''
1차시도
i를 min(nums)fh 잡고 [i+1:]에서 j를 잡는방식-> triplet이 있어도 min(nums)가 포함 안될수도 있음
For 문 돌면서 nums[i], nums[j]값을 업데이트 시키는 방식으로 변경. 
num < first num <= second 
test case: [1,1,-2,6]
=> i,j 모두 1로 업데이트됨 -> j가 다시 -2로 업데이트 되면서 조건 만족 x

2차시도 
num<=first 
num<=second
'''