class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {} #값:인덱스
        
        for i, num1 in enumerate(nums):
            num2 = target - num1  #num1과의 합이 target이 되는 num2 
            
            if num2 in seen: 
                #seen 안에 있으면 seen[값]= num2 인덱스 , num1 인덱스=i return
                return [seen[num2], i]
            
            seen[num1] = i #seen 안에 없으면 일단 기록
