class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int


        """
        i=0
        j=len(height)-1
        maxArea=0
        while i<j:
            currentArea=min(height[i],height[j])*(j-i)
            maxArea = max(maxArea, currentArea)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1

        return maxArea

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))