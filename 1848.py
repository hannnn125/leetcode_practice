class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        
        ls = []
        for i in range(len(nums)):
            if nums[i]==target:
                ls.append(i)

        minimum = min(abs(i-start) for i in ls)
        
        return minimum
        
