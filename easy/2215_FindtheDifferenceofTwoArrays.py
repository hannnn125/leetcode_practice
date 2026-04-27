class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        numls1=[x for x in nums1 if x not in nums2]
        numls2=[x for x in nums2 if x not in nums1]
        return [numls1,numls2]
         

nums1=[1,2,3]
nums2=[2,4,6]

print(Solution().findDifference(nums1,nums2))
