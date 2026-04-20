class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # 리스트 내 가장 큰 value를 찾아서 extraCandies를 더한 값이 이를 넘으면 true, 아니면 false 를 리스트에 추가하여 반환
        result = []
        for i in candies: 
            if  i+extraCandies >= max(candies):
                result.append(True)
            else: 
                result.append(False)
        return result